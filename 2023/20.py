import abc
import dataclasses
import re
import math as m
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Optional

data = open('d/20').read().strip()
# data = '''
# broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a
# '''.strip()
# data = '''
# broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output
# '''.strip()


@dataclass
class Module(abc.ABC):
    destination: list[str]

    def add_source(self, source: str):
        pass

    @abc.abstractmethod
    def pulse(self, source: str, is_low: bool) -> Optional[bool]:
        pass


@dataclass
class BroadcastModule(Module):
    def pulse(self, source: str, is_low: bool):
        assert is_low == True
        return True


@dataclass
class FlipFlopModule(Module):
    is_on: bool = False

    def pulse(self, source: str, is_low: bool) -> Optional[bool]:
        if not is_low:
            return None
        if is_low:
            self.is_on = not self.is_on
        return not self.is_on


@dataclass
class Conjunction(Module):
    inputs_low: dict[str, bool] = dataclasses.field(default_factory=lambda: {})

    def add_source(self, source: str):
        self.inputs_low[source] = True

    def pulse(self, source: str, is_low: bool) -> Optional[bool]:
        # if all are false => true
        # if any is true => false
        self.inputs_low[source] = is_low
        return not any(self.inputs_low.values())


modules = {}
for typ, name, dest in re.findall(r'([%&]?)(\w+) -> ([\w, ]+)', data):
    destination = dest.split(', ')
    if typ == '':
        modules[name] = BroadcastModule(destination=destination)
    if typ == '%':
        modules[name] = FlipFlopModule(destination=destination)
    if typ == '&':
        modules[name] = Conjunction(destination=destination)

for src, mod in modules.items():
    for n in mod.destination:
        if n in modules:
            modules[n].add_source(src)
        # else:
        #     print(f"Untyped: {n}")


def solve(n):
    pulse_counts = {True: 0, False: 0}
    done = [False]
    i = 0

    def press_button():
        pulses = [('button', 'broadcaster', True)]
        while pulses:
            source, dest, val = pulses.pop()
            if dest == 'rx' and val:
                done[0] = True
            # print(source, '-low->' if val else '-high>', name,)
            pulse_counts[val] += 1
            if dest not in modules:
                continue
            output = modules[dest].pulse(source, val)
            if dest == 'vr' and not val:
                print(i, modules['vr'])
            pulses = [(dest, d, output) for d in reversed(modules[dest].destination) if output is not None] + pulses

    previous_states = {}

    while not done[0]:
    # for i in range(n):
        i += 1
        press_button()
        # print(repr(modules['vr']))
        # s = repr(modules)
        # if s in previous_states:
        #     period = i - previous_states[s]
        #     remaining = (n - i - 1) % period
        #     print('period', period, 'remaining', remaining)
        #     for _ in range(remaining):
        #         press_button()
        #     break
        # else:
        #     previous_states[s] = i
    return i
    #return m.prod(pulse_counts.values())

# 32000000
# 11687500
# 712543680
print(solve(1000))
