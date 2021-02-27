

"""
Author: Ron Nathaniel      [rn328@njit.edu]
Professor: Shaheer Haroon  [sharoon@njit.edu]
Semester: Spring 2021
Date: Feb 26 2021
Assignment: A1
"""

# Set by output flag, determines level of verbosity
DEBUG = False


# Actual logging, determined by level of debugging
def log(*s):
    global DEBUG
    if DEBUG:
        print(*s)


# better inputting, with defaults, conversions, error handing, and formatting
def ask(s, convert_type=None, default='', error_msg='', space=' ', options=''):
    try:
        res = input(s + '? ' + options + (' [{d}]'.format(d=default) if default else '') + space) or default
        if convert_type:
            res = convert_type(res)
        return res
    except Exception as e:
        print(error_msg)
        print(e)
        return default


# instance of domino or string of dominoes.
class Domino:
    def __init__(self, num, den):
        if isinstance(num, str):
            num = [num]
        if isinstance(den, str):
            den = [den]

        # num and den both lists to allow separation of dominoes
        self.num = num
        self.den = den

    # combine two domino instances, returns a new instance
    def add(self, d):
        n = self.num + d.num
        d = self.den + d.den
        return Domino(n, d)

    # numerator as sequential string
    def numer(self):
        return ''.join(self.num)

    # denominator as sequential string
    def denom(self):
        return ''.join(self.den)

    # determines if one half is a prefix of another
    def is_accepting(self):
        return (
                self.numer().startswith(self.denom())
                or
                self.denom().startswith(self.numer())
        )

    # determines if both hals are equal
    def is_finished(self):
        return self.numer() == self.denom()

    # override equality based on total strings
    def __eq__(self, other):
        if isinstance(other, Domino):
            return (
                self.numer() == other.numer()
                and
                self.denom() == other.denom()
            )

    # override to_string for formatting
    def __repr__(self):
        return '{n} - {d}'.format(n=self.numer(), d=self.denom())


# search a list of Dominos for a solution for the
# Post Correspondence Problem
# dominoes: list of dominoes
# max_frontier size and max_state size configurable
def search(dominoes, max_frontier_t=300, max_states_t=300):
    # set all visited dominoes so far
    states = frontier = [*dominoes]
    move_to_deep = False

    log('------ Filling Frontier ------')

    while frontier:
        # get another domino from frontier
        current = frontier.pop()
        log('Removing State from Frontier:', current)

        # try all dominoes to look for solution
        for next_domin in dominoes:
            combined = current.add(next_domin)

            # if new and accepting, add it to frontier
            if combined not in states and combined.is_accepting() and not move_to_deep:
                states.append(combined)
                frontier.insert(0, combined)
                log('Adding State to Frontier:', combined)

            # if in finished state, solution found
            if combined.is_finished():
                log('------ Frontier Complete ------')

                # stage is determined by move_to_deep
                if not move_to_deep:
                    print('Solution found in Stage 1')
                # moved to iterative deepening
                else:
                    print('Solution found in Stage 2 Iterative Deepening')
                print('Solution Size (# of dominoes): ', len(combined.num))

                # combine all numerators and denominators as a list in order
                solution = list(zip(combined.num, combined.den))
                path = Domino('', '')

                for i, s in enumerate(solution):
                    # add domino to path in order
                    d = Domino(*s)
                    print('step #', i+1,  ': ', d)
                    path = path.add(d)

                print('total sequence: ', path)
                return

            # exhausted limits. Moving to stage 2
            if len(states) > max_depth_t or len(frontier) > max_frontier_t and not move_to_deep:
                print('Exceeded configuration limit.')
                print('Popping state from stack')
                print(states)
                move_to_deep = True
                break

    # if have not left yet, no solution was found.
    print('No solution found.')


if __name__ == '__main__':
    # input args from user
    max_frontier_t = ask('Max frontier size', default=5, convert_type=int)
    max_depth_t = ask('Max number of states', default=50, convert_type=int)
    output_flag = ask('Output flag', convert_type=int, default='0', options='0-1')
    if output_flag:
        # set global debug flag
        print(output_flag)
        DEBUG = True
        print('Turning debugging logs on.')


    dominoes = []
    num_domin = ask('How many dominoes', convert_type=int, default=3)
    print('List each domino with a space sep. ex: aa bb')
    for i in range(1, num_domin + 1):
        d = ask(str(i))
        # if not domino inputted, stop asking and move on
        if not d:
            break
        d = d.split(' ')
        dominoes.append(Domino(*d))
    print()

    search(dominoes, max_frontier_t, max_depth_t)

