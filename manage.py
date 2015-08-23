from __future__ import print_function

import subprocess
import os
import glob
import shutil
import argparse
import sys


def call(cmd_string):
    subprocess.check_call(cmd_string.split())


def call_git_clean():
    call('git clean -fdx')


def call_pdflatex():
    cmd_string = 'pdflatex --interaction=nonstopmode thesis.tex'
    process = subprocess.Popen(cmd_string.split(), stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    try:
        process.communicate(timeout=10)
    except subprocess.TimeoutExpired as e:
        print('ERROR! Try to run "{}"" manually to debug'.format(cmd_string))
        sys.exit(1)


def call_biber():
    call('biber thesis.bcf')


def get_my_short_commit_hash():
    output = subprocess.check_output('git rev-parse --short HEAD'.split())
    return output.strip().decode()


def build_pdf():
    print('Building PDF')
    call_pdflatex()
    call_pdflatex()
    call_biber()
    call_pdflatex()
    # Rename the file to contain the commit hash
    commit = get_my_short_commit_hash()
    new_name = 'thesis_{}.pdf'.format(commit)
    os.rename('thesis.pdf', new_name)
    print('PDF building finished succesfully!')


def build_graphics():
    print('Building graphics')
    for filename in os.listdir('graphics'):
        if os.path.splitext(filename)[1] == '.svg':
            path = os.path.join('graphics', filename)
            build_single_svg(path)
    print('Graphics building finished succesfully!')


def build_single_svg(path):
    new_path = '{}.{}'.format(os.path.splitext(path)[0], 'pdf')
    cmd_template = 'inkscape -D -z --file={} --export-pdf={} --export-latex'
    cmd_string = cmd_template.format(path, new_path)
    call(cmd_string)


def copy_globs(glob_src, dest_dir):
    for path in glob.glob(glob_src):
        shutil.copy(path, dest_dir)


def get_plots_and_update_commit():
    get_plots()
    write_analysis_commit_to_repo()


def get_plots():
    src = '../exp/analysis/graphics'
    dst = 'plots'
    print('Copying plots from "{}" to "{}"...'.format(src, dst))
    if dst in os.listdir('.'):
        shutil.rmtree(dst)  # Remove the current directory first
    os.mkdir(dst)
    glob_pattern = os.path.join(src, '*.pdf')
    copy_globs(glob_pattern, dst)
    print('Got all plots!')


def get_analysis_commit():
    path_to_commit_hash = '../exp/analysis/.git/refs/heads/master'
    with open(path_to_commit_hash) as f:
        return f.read().strip()


def write_analysis_commit_to_repo():
    commit = get_analysis_commit()
    print('The commit hash of the remote git repo is {}'.format(commit))
    print('Writing it to "analysis_commit_hash"')
    with open('analysis_commit_hash', 'w') as f:
        f.write(commit + '\n')


def parse_option():
    choices = ['clean', 'graphics', 'plots', 'pdf', 'all']
    parser = argparse.ArgumentParser(description='Management commands')
    parser.add_argument('option', metavar='Option', type=str,
                        choices=choices, help='option to run')
    args = parser.parse_args()
    return args.option


def full_run():
    call_git_clean()
    build_graphics()
    get_plots_and_update_commit()
    build_pdf()


def main():
    choice_to_func = {
        'clean': call_git_clean,
        'graphics': build_graphics,
        'plots': get_plots_and_update_commit,
        'pdf': build_pdf,
        'all': full_run,
    }
    choice = parse_option()
    choice_to_func[choice]()


if __name__ == '__main__':
    main()
