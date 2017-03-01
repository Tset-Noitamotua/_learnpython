# -*- coding: utf-8 -*-

from __future__ import print_function

import functools
import random
import sys
import time

import progressbar

examples = []

non_interactive_sleep_factor = 100
range_count = 500000


def sleep(delay):
    '''Make non-interactive examples faster by a factor'''
    if __name__ != '__main__':
        delay /= non_interactive_sleep_factor
    time.sleep(delay)


def example(fn):
    '''Wrap the examples so they generate readable output'''

    @functools.wraps(fn)
    def wrapped():
        try:
            sys.stdout.write('Running: %s\n' % fn.__name__)
            fn()
            sys.stdout.write('\n')
        except KeyboardInterrupt:
            sys.stdout.write('\nSkipping example.\n\n')
            # Sleep a bit to make killing the script easier
            time.sleep(0.2)

    examples.append(wrapped)
    return wrapped

def del_from_list():
    values = [x for x in range(100)]
    del values[95]
    # if len(values) != 99: break

def remove_from_list():
    values = [x for x in range(100)]
    values.remove(95)
    # if len(values) != 99: break


@example
def without_progress_bar():
    timer_start = time.time()
    for i in range(range_count):
        del_from_list()
    timer_stop = time.time()
    print('del - done in %i s' %(timer_stop - timer_start))

    timer_start = time.time()
    for i in range(range_count):
        remove_from_list()
    timer_stop = time.time()
    print('remove() - done in %i s' %(timer_stop - timer_start))


@example
def with_example():
    print('\n- del -')
    with progressbar.ProgressBar(max_value=range_count) as progress:
        for i in range(range_count):
            # do something
            del_from_list()
            progress.update(i)

    print('\n- remove() -')
    with progressbar.ProgressBar(max_value=range_count) as progress:
        for i in range(range_count):
            # do something
            remove_from_list()
            progress.update(i)


@example
def with_example_wo_comments():
    print('\n- del -')
    with progressbar.ProgressBar(max_value=range_count) as progress:
        for i in range(range_count):
            # do something
            del_from_list()
            progress.update(i)

    print('\n- remove() -')
    with progressbar.ProgressBar(max_value=range_count) as progress:
        for i in range(range_count):
            # do something
            remove_from_list()
            progress.update(i)


@example
def with_example_stdout_redirection():
    with progressbar.ProgressBar(max_value=range_count, redirect_stdout=True) as p:
        for i in range(range_count):
            #do something
            del_from_list()
            p.update(i)


@example
def basic_widget_example():
    widgets = [progressbar.Percentage(), progressbar.Bar()]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=range_count).start()
    for i in range(range_count):
        # do something
        del_from_list()
        bar.update(i + 1)
    bar.finish()


@example
def file_transfer_example():
    widgets = [
        'Test: ', progressbar.Percentage(),
        ' ', progressbar.Bar(marker=progressbar.RotatingMarker()),
        ' ', progressbar.ETA(),
        ' ', progressbar.FileTransferSpeed(),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=10000000).start()
    for i in range(range_count):
        # do something
        del_from_list()
        bar.update(10 * i + 1)
    bar.finish()


@example
def custom_file_transfer_example():
    class CrazyFileTransferSpeed(progressbar.FileTransferSpeed):

        "It's bigger between 45 and 80 percent"

        def update(self, bar):
            if 45 < bar.percentage() < 80:
                return 'Bigger Now ' + progressbar.FileTransferSpeed.update(
                    self, bar)
            else:
                return progressbar.FileTransferSpeed.update(self, bar)

    widgets = [
        CrazyFileTransferSpeed(),
        ' <<<', progressbar.Bar(), '>>> ',
        progressbar.Percentage(),
        ' ',
        progressbar.ETA(),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=10000000)
    # maybe do something
    bar.start()
    for i in range(range_count):
        # do something
        del_from_list()
        bar.update(5 * i + 1)
    bar.finish()


@example
def double_bar_example():
    widgets = [
        progressbar.Bar('>'), ' ',
        progressbar.ETA(), ' ',
        progressbar.ReverseBar('<'),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=10000000).start()
    for i in range(range_count):
        # do something
        del_from_list()
        bar.update(10 * i + 1)
    bar.finish()


@example
def basic_file_transfer():
    widgets = [
        'del: ', progressbar.Percentage(),
        ' ', progressbar.Bar(marker='-', left='[', right=']'),
        ' ', progressbar.ETA(),
        ' ', progressbar.FileTransferSpeed(),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=range_count)
    bar.start()
    # Go beyond the max_value
    for i in range(0, (range_count + 1), 1):
        # do something
        del_from_list()
        bar.update(i)
    bar.finish()

    widgets = [
        'remove: ', progressbar.Percentage(),
        ' ', progressbar.Bar(marker='>', left='[', right=']'),
        ' ', progressbar.ETA(),
        ' ', progressbar.FileTransferSpeed(),
    ]
    bar = progressbar.ProgressBar(widgets=widgets, max_value=range_count)
    bar.start()
    # Go beyond the max_value
    for i in range(0, (range_count + 1), 1):
        # do something
        remove_from_list()
        bar.update(i)
    bar.finish()


@example
def simple_progress():
    bar = progressbar.ProgressBar(
        widgets=[progressbar.SimpleProgress()],
        max_value=range_count,
    ).start()
    for i in range(range_count):
        # do something
        del_from_list()
        bar.update(i + 1)
    bar.finish()


@example
def basic_progress():
    bar = progressbar.ProgressBar(max_value=1000000).start()
    for i in range(range_count):
        # do something
        del_from_list()
        bar.update(i + 1)
    bar.finish()


@example
def progress_with_automatic_max():
    # Progressbar can guess max_value automatically.
    bar = progressbar.ProgressBar()
    for i in bar(range(range_count)):
        #do something
        del_from_list()


@example
def progress_with_unavailable_max():
    # Progressbar can't guess max_value.
    bar = progressbar.ProgressBar(max_value=range_count)
    for i in bar((i for i in range(range_count))):
        # do something
        del_from_list()


@example
def animated_marker():
    bar = progressbar.ProgressBar(
        widgets=['Working: ', progressbar.AnimatedMarker()])
    for i in bar((i for i in range(range_count))):
        # do something
        del_from_list()


@example
def counter_and_timer():
    widgets = ['Processed: ', progressbar.Counter(),
               ' lines (', progressbar.Timer(), ')']
    bar = progressbar.ProgressBar(widgets=widgets)
    for i in bar((i for i in range(range_count))):
        del_from_list()


@example
def format_label():
    widgets = [progressbar.FormatLabel(
        'Processed: %(value)d lines (in: %(elapsed)s)')]
    bar = progressbar.ProgressBar(widgets=widgets)
    for i in bar((i for i in range(range_count))):
        del_from_list()


@example
def animated_balloons():
    widgets = ['Balloon: ', progressbar.AnimatedMarker(markers='.oO@* ')]
    bar = progressbar.ProgressBar(widgets=widgets)
    for i in bar((i for i in range(range_count))):
        del_from_list()


@example
def format_label_bouncer():
    widgets = [
        progressbar.FormatLabel('Bouncer: value %(value)d - '),
        progressbar.BouncingBar(),
    ]
    bar = progressbar.ProgressBar(widgets=widgets)
    for i in bar((i for i in range(range_count))):
        del_from_list()


@example
def format_label_rotating_bouncer():
    widgets = [progressbar.FormatLabel('Animated Bouncer: value %(value)d - '),
               progressbar.BouncingBar(marker=progressbar.RotatingMarker())]

    bar = progressbar.ProgressBar(widgets=widgets)
    for i in bar((i for i in range(range_count))):
        del_from_list()


@example
def with_right_justify():
    with progressbar.ProgressBar(max_value=range_count, term_width=20,
                                 left_justify=False) as progress:
        assert progress.term_width is not None
        for i in range(range_count):
            del_from_list()
            progress.update(i)







@example
def rotating_bouncing_marker():
    widgets = [progressbar.BouncingBar(marker=progressbar.RotatingMarker())]
    with progressbar.ProgressBar(widgets=widgets, max_value=range_count,
                                 term_width=10) as progress:
        for i in range(range_count):
            del_from_list()
            progress.update(i)

    widgets = [progressbar.BouncingBar(marker=progressbar.RotatingMarker(),
                                       fill_left=False)]
    with progressbar.ProgressBar(widgets=widgets, max_value=range_count,
                                 term_width=10) as progress:
        for i in range(range_count):
            del_from_list()
            progress.update(i)


@example
def incrementing_bar():
    bar = progressbar.ProgressBar(widgets=[
        progressbar.Percentage(),
        progressbar.Bar(),
    ], max_value=range_count).start()
    for i in range(range_count):
        # do something
        del_from_list()
        bar += 1
    bar.finish()


# @example
# def eta_types_demonstration():
#     widgets = [
#         progressbar.Percentage(),
#         ' ETA: ', progressbar.ETA(),
#         ' Adaptive ETA: ', progressbar.AdaptiveETA(),
#         ' Absolute ETA: ', progressbar.AbsoluteETA(),
#         ' Adaptive Transfer Speed: ', progressbar.AdaptiveTransferSpeed(),
#         ' ', progressbar.Bar(),
#     ]
#     bar = progressbar.ProgressBar(widgets=widgets, max_value=500)
#     bar.start()
#     for i in range(500):
#         if i < 100:
#             sleep(0.02)
#         elif i > 400:
#             sleep(0.1)
#         else:
#             sleep(0.01)
#         bar.update(i + 1)
#     bar.finish()


@example
def adaptive_eta_without_value_change():
    # Testing progressbar.AdaptiveETA when the value doesn't actually change
    bar = progressbar.ProgressBar(widgets=[
        progressbar.AdaptiveETA(),
        progressbar.AdaptiveTransferSpeed(),
    ], max_value=range_count, poll=0.0001)
    bar.start()
    for i in range(range_count):
        bar.update(1)
        del_from_list()
    bar.finish()


@example
def iterator_with_max_value():
    # Testing using progressbar as an iterator with a max value
    bar = progressbar.ProgressBar()

    for n in bar(iter(range(range_count)), range_count):
        # iter range is a way to get an iterator in both python 2 and 3
        del_from_list()


# @example
# def eta():
#     widgets = [
#         'Test: ', progressbar.Percentage(),
#         ' | ETA: ', progressbar.ETA(),
#         ' | AbsoluteETA: ', progressbar.AbsoluteETA(),
#         ' | AdaptiveETA: ', progressbar.AdaptiveETA(),
#     ]
#     bar = progressbar.ProgressBar(widgets=widgets, maxval=range_count).start()
#     for i in range(range_count):
#         del_from_list()
#         bar.update(i + 1)
#     bar.finish()


@example
def dynamic_message():
    # Use progressbar.DynamicMessage to keep track of some parameter(s) during
    # your calculations
    widgets = [
        progressbar.Percentage(),
        progressbar.Bar(),
        progressbar.DynamicMessage('loss'),
    ]
    with progressbar.ProgressBar(max_value=range_count, widgets=widgets) as bar:
        min_so_far = 1
        for i in range(range_count):
            val = random.random()
            if val < min_so_far:
                min_so_far = val
            bar.update(i, loss=min_so_far)


@example
def format_custom_text():
    # - del - 
    format_custom_text = progressbar.FormatCustomText(
        ' %(func_name)s, items: %(eggs)d',
        dict(
            func_name='del',
            eggs=0,
        ),
    )

    bar = progressbar.ProgressBar(widgets=[
        progressbar.Percentage(),
        format_custom_text, ' ',
        progressbar.Bar(), ' ',
        progressbar.Timer(),
    ])
    for i in bar(range(range_count + 1)):
        format_custom_text.update_mapping(eggs=i * 1)
        del_from_list()

    # - remove() - 
    format_custom_text = progressbar.FormatCustomText(
        ' %(func_name)s, items: %(eggs)d',
        dict(
            func_name='remove()',
            eggs=0,
        ),
    )

    bar = progressbar.ProgressBar(widgets=[
        progressbar.Percentage(),
        format_custom_text, ' ',
        progressbar.Bar(), ' ',
        progressbar.Timer(),
    ])
    for i in bar(range(range_count + 1)):
        format_custom_text.update_mapping(eggs=i * 1)
        remove_from_list()


@example
def simple_api_example():
    bar = progressbar.ProgressBar(widget_kwargs=dict(fill='█'))
    for i in bar(range(range_count)):
        del_from_list()
    
    bar = progressbar.ProgressBar(widget_kwargs=dict(fill='█'))
    for i in bar(range(range_count)):
        remove_from_list()


# @example
# def ETA_on_generators():
#     def gen():
#         for x in range(range_count):
#             yield None

#     widgets = [progressbar.AdaptiveETA(), ' ',
#                progressbar.ETA(), ' ',
#                progressbar.Timer()]

#     bar = progressbar.ProgressBar(widgets=widgets)
#     for i in bar(gen()):
#         del_from_list()


# @example
# def percentage_on_generators():
#     def gen():
#         for x in range(range_count):
#             yield None

#     widgets = [progressbar.Counter(), ' ',
#                progressbar.Percentage(), ' ',
#                progressbar.SimpleProgress(), ' ']

#     bar = progressbar.ProgressBar(widgets=widgets)
#     for i in bar(gen()):
#         del_from_list()


def test(*tests):
    for example in examples:
        if not tests or example.__name__ in tests:
            example()
        else:
            print('Skipping', example.__name__)


if __name__ == '__main__':
    try:
        test(*sys.argv[1:])
    except KeyboardInterrupt:
        sys.stdout('\nQuitting examples.\n')
