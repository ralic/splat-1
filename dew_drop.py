# Splat - dew_drop.py
#
# Copyright (C) 2012, 2013 Guillaume Tucker <guillaume@mangoz.org>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import time
import argparse
import splat
import splat.data
import splat.gen
import splat.filters
import splat.scales
from splat import dB2lin as dB

def set_fade(gen, duration):
    gen.filters = splat.filters.FilterChain(
        [(splat.filters.linear_fade, (duration,))])

def main(argv):
    parser = argparse.ArgumentParser("Dew Drop tune using irrational rythm.")
    parser.add_argument('--save-as', default='dew_drop.wav',
                        help="output file name, leave blank to not save")
    parser.add_argument('--no-reverb', action='store_true',
                        help="do not generate the reverb effect")
    parser.add_argument('--dump-scale', action='store_true',
                        help="dump the frequency of the notes in the scale")
    parser.add_argument('--rate', type=int, default=48000,
                        help="sample rate")
    parser.add_argument('--voices', default='123',
                        help="voices to run (string with 1, 2 and 3)")
    args = parser.parse_args(argv[1:])

    gen = splat.gen.OvertonesGenerator(splat.data.Fragment(2, args.rate, 18.0))
    s = splat.scales.LogScale(fund=440.0)

    if args.dump_scale is True:
        # print frequencies of all the notes of the scale over 3 octaves
        for octave in range(-2, 1):
            for note in ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']:
                note_name = "{0}{1}".format(note, octave)
                print('{0:4s}: {1:.3f}'.format(note_name, s[note_name]))
            print("-------------")

    if '1' in args.voices:
        print("Voice 1")
        gen.levels = (dB(-2.5), dB(-2.5))
        gen.ot_decexp(2.0)
        set_fade(gen, 0.04)
        gen.run(0.0, 1.62, s['A-2'])
        gen.run(1.62, 3.24, s['D-2'])
        gen.run(3.24, 4.248, s['F#-2'])
        gen.run(4.248, 5.868, s['E-2'])
        gen.run(5.868, 6.858, s['D-2'])
        gen.run(6.858, 8.496, s['F#-2'])
        gen.run(8.496, 9.504, s['E-2'])
        gen.run(9.504, 11.124, s['B-2'])
        gen.run(11.124, 12.744, s['E-2'])
        gen.run(12.744, 13.752, s['A-2'])
        gen.run(13.752, 14.742, s['D-2'])
        gen.run(14.742, 16.38, s['E-2'])
        gen.run(16.38, 18.0, s['A-2'])

    if '2' in args.voices:
        print("Voice 2")
        gen.levels = (dB(0.0), dB(-2.5))
        gen.ot_decexp(1.6)
        set_fade(gen, 0.02)
        gen.run(0.0, 1.008, s['C#-1'])
        gen.run(1.008, 1.62, s['E-1'])
        gen.run(1.62, 2.628, s['A-1'])
        gen.run(2.628, 3.24, s['F#-2'])
        gen.run(3.24, 3.852, s['A-1'])
        gen.run(3.852, 4.248, s['C#-1'])
        gen.run(4.248, 4.86, s['B-1'])
        gen.run(4.86, 5.868, s['D-1'])
        gen.run(5.868, 6.858, s['B-1'])
        gen.run(6.858, 7.848, s['C#-1'])
        gen.run(7.848, 8.496, s['A-1'])
        gen.run(8.496, 9.504, s['G#-2'])
        gen.run(9.504, 10.494, s['D-1'])
        gen.run(10.494, 11.124, s['F#-1'])
        gen.run(11.124, 11.754, s['B-1'])
        gen.run(11.754, 12.744, s['D-1'])
        gen.run(12.744, 13.752, s['E-1'])
        gen.run(13.752, 14.364, s['F#-1'])
        gen.run(14.364, 15.372, s['A-1'])
        gen.run(15.372, 16.38, s['D-1'])
        gen.run(16.38, 18.0, s['C#-1'])

    if '3' in args.voices:
        print("Voice 3")
        gen.levels = (dB(-2.5), dB(0.0))
        gen.ot_decexp(1.2)
        set_fade(gen, 0.015)
        gen.run(0.0, 0.612, s['E'])
        gen.run(0.612, 1.008, s['D'])
        gen.run(1.008, 1.62, s['E'])
        gen.run(1.62, 2.232, s['D'])
        gen.run(3.24, 3.852, s['C#'])
        gen.run(3.852, 4.248, s['A'])
        gen.run(4.248, 4.86, s['B'])
        gen.run(4.86, 5.256, s['D'])
        gen.run(5.256, 5.868, s['E'])
        gen.run(5.868, 6.858, s['F#'])
        gen.run(8.496, 8.874, s['D'])
        gen.run(8.874, 9.504, s['E'])
        gen.run(9.504, 10.494, s['F#'])
        gen.run(10.494, 11.124, s['A'])
        gen.run(11.124, 11.754, s['B'])
        gen.run(11.754, 12.132, s['C#'])
        gen.run(12.132, 12.744, s['D'])
        gen.run(12.744, 13.752, s['C#'])
        gen.run(14.364, 15.372, s['B'])
        gen.run(15.372, 16.38, s['G#-1'])
        gen.run(16.38, 18.0, s['A'])

    if args.no_reverb is False:
        print("Reverb")
        d = splat.filters.reverb_delays()
        splat.filters.reverb(gen.frag, d)

    if args.save_as:
        print("Saving as {}".format(args.save_as))
        padded = splat.data.Fragment(2, args.rate, (gen.frag.duration + 1.0))
        padded.mix(gen.frag, 0.5)
        padded.save(args.save_as)


if __name__ == '__main__':
    start = time.time()
    main(sys.argv)
    stop = time.time()
    print("Total time: {0:.3f}".format(stop - start))
    sys.exit(0)
