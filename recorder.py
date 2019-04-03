#!/usr/bin/env python
"""Record what and where been created runtime."""

# TODO
# * set settrace to function which checks __init__ calls
# * get source of class and MRO
# * write it to log file (later convert into db)
#
# * simple and dirty way:
# record what was created before return
#
# GOAL:
# select * from assigments where lname = 'name';
# aleph.TheSimpleOne.__init__:16
# aleph.TheSimpleOne.set_name:
# aleph.TheSimpleOne.__str__
# aleph.some_function
import sys
import linecache



def trace_lines(frame, event, arg):
    """
    # XXX
    check that https://docs.python.org/2/library/inspect.html
    - bytecode of that line is assigment
    - iteratively check that there is no new var in locals of type TYPE
    - write to DB the whole line
    """
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    print('*  {} line {}'.format(func_name, line_no))
    line = linecache.getline(co.co_filename, line_no)
    print(f'line is: {line}')

def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    if func_name == 'some_function':
        return trace_lines
    # print('* Call to {} on line {} of {}'.format(func_name, line_no, filename))
    return


def main():
    from aleph import some_function
    some_function('one')

sys.settrace(trace_calls)
main()
