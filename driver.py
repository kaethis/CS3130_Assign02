#!/usr/bin/env python3

import sys

import parser 

import ui


filename = ''

errors = { 'INVSYN' : 'INVALID SYNTAX!',
           'NOFILE' : 'FILE NOT FOUND!' }


def main():

    collect = []

    for key in parser.collect.keys(): collect.append(parser.collect[key])


    y, x = 1, 2

    height = 20 

    while True:

        ret = ui.menuwin(y, x, height, 0, parser.schema, collect) 

        if ui.confirm(y, x, 'EXIT?') == 0: break


    ui.exit()

    quit()


if __name__ == '__main__':

    if not len(sys.argv) == 2:

        ui.exit();

        print('[ERROR] '+errors['INVSYN']+'\n')

        print('[USAGE] \''+sys.argv[0]+' filename.txt\'')

        quit();

    else:

        filename = sys.argv[1]

        ex = '[A-Za-z]+\'*[A-Za-z]+|[A-Za-z]+'

        if parser.parse(filename, ex) == -1:

            ui.exit();

            print('[ERROR] \''+filename+'\' '+errors['NOFILE']+'\n');

            quit();


        main();
