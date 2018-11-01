import os
import re
import math
import shutil
import argparse
import subprocess

def get_args():
    parser = argparse.ArgumentParser(description='Nand2Tetris Grader')

    # Required positional argument
    parser.add_argument('project_base', help='path to nand2tetris')
    parser.add_argument('project_index', help='index of project')
    parser.add_argument('tool', help='name of tool (in project_base/tools)')
    parser.add_argument('folder_suffix_regex', help='')
    parser.add_argument('--max-score', type=float, help='max score', default=100)

    return parser.parse_args()

def get_source_for_test(testpath):
    with open(testpath) as f:
        for line in f:
            line = line.strip()
            if 'load' in line:
                filename = line.split(' ')[1][:-1]
                return filename
    raise RuntimeError('Impossible path. Something went wrong.')

def prepare_test_source_pair(project_folder):
    tests = {}
    with os.scandir(project_folder) as content:
        for c in content:
            if c.name.endswith('.tst'):
                testpath = os.path.join(project_folder, c.name)
                tests[c.name] = get_source_for_test(testpath)
    return tests

def find_target_dir(entry, folder_suffix_regex):
    with os.scandir(entry) as content:
        pattern = '{}{}'.format(entry.name, folder_suffix_regex)
        for c in content:
            if c.is_dir() and re.match(pattern, c.name, re.IGNORECASE):
                return c
    return None

def copy_test_related_file(project_folder):
    with os.scandir(project_folder) as content:
        for c in content:
            if c.name.endswith('.tst') or c.name.endswith('.cmp') or c.name.endswith('.hack'):
                filepath = os.path.join(project_folder, c.name)
                shutil.copy(filepath, '.')

def cleanup():
    with os.scandir('.') as content:
        for c in content:
            if c.name.endswith('.out'):
                os.remove(c.name)

def test_handle_corner_case(args, project_base, testfile, sourcefile):
    if args.project_index == '05' and testfile == 'Memory.tst':
        print('** need manual check\n')
        return True
    elif args.project_index.startswith('04'):
        tool = os.path.join(project_base, 'tools', 'Assembler.sh')

        try:
            asmfile = '{}.asm'.format(sourcefile.split('.')[0])
            cmd = '{} {}'.format(tool, asmfile)
            result = subprocess.check_output(
                    cmd,
                    stderr=subprocess.STDOUT,
                    shell=True)
            print(result.decode())
        except subprocess.CalledProcessError as e:
            print(e.output.decode())

        if testfile == 'Fill.tst':
            print('** need manual check\n')
            return True

def main(args):
    project_base = os.path.realpath(args.project_base)
    project_folder = os.path.join(project_base, 'projects', args.project_index)
    tool = os.path.join(project_base, 'tools', args.tool)

    tests = prepare_test_source_pair(project_folder)
    score_per_test = 1.0 / len(tests) * args.max_score

    with os.scandir('.') as it:
        for entry in it:
            if not entry.is_dir():
                continue

            print('=' * 80)
            print(entry.name)
            target_dir = find_target_dir(entry, args.folder_suffix_regex)
            if target_dir is None:
                for stuff in os.listdir(entry.name):
                    print(stuff)
                print('[{}] folder format incorrect'.format(entry.name))
                continue

            cwd = os.getcwd()

            # pushd
            os.chdir(os.path.join(cwd, entry.name, target_dir.name))

            copy_test_related_file(project_folder)
            cleanup()

            correct_cnt = 0
            for test, source in tests.items():
                print('{} ({:.1f}):'.format(test, score_per_test))

                if test_handle_corner_case(args, project_base, test, source):
                    continue

                if not os.path.isfile(source):
                    print('{} not exists'.format(source))
                    continue

                try:
                    result = subprocess.check_output(
                            '{} {}'.format(tool, test),
                            stderr=subprocess.STDOUT,
                            shell=True)
                    print(result.decode())
                    correct_cnt += 1
                except subprocess.CalledProcessError as e:
                    print(e.output.decode())

            score = float(correct_cnt) * score_per_test
            print('[{}] {:.1f}'.format(entry.name, score))
            # popd
            os.chdir(cwd)

if __name__ == '__main__':
    main(get_args())
