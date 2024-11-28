from lib.regex import parse_numbers
from lib.math import get_nth_digit


class Intcode:
    def __init__(self, program: list[int]):
        self.pointer = 0
        self.initial_program = program.copy()  # For resetting
        self.program = program.copy()
        self.current_instruction = 0

    def _read_next(self):
        """Read next integer from pointer position, and move pointer one step."""
        output = self.program[self.pointer]
        self.pointer += 1
        return output

    def _read(self, num_positions: int):
        """Read `num_positions` integers from pointer position, and move pointer accordingly."""
        output = self.program[self.pointer : self.pointer + num_positions]
        self.pointer += num_positions
        return output

    def _get_param(self, parameter_position=2):
        value = self._read_next()

        match get_nth_digit(self.current_instruction, parameter_position):
            case 0:  # Position mode
                return self.program[value]
            case 1:  # Immediate mode
                return value
            case _ as parameter_mode:
                raise ValueError(f"Parameter mode {parameter_mode} not recognized")

    def _get_params(self, num_params: int):
        parameter_position = 2
        params: list[int] = []

        for _ in range(num_params):
            param = self._get_param(parameter_position)
            params.append(param)
            parameter_position += 1

        return params

    def run(self, program_input: int | None = None, reset=False):
        program_output = None

        while True:
            self.current_instruction = self._read_next()

            match self.current_instruction % 100:
                # Day 2
                case 1 | 2 as opcode:
                    # Add (1) or multiply (2) the numbers at positions p1 and p2 and write the output to p3
                    p1, p2 = self._get_params(2)
                    p3 = self._read_next()

                    self.program[p3] = p1 + p2 if opcode == 1 else p1 * p2

                # Day 5, part a
                case 3:  # Write input to position p1
                    p1 = self._read_next()

                    if not isinstance(program_input, int):
                        raise ValueError("Integer input required for write action")

                    self.program[p1] = program_input
                case 4:  # Write parameter value to output
                    program_output = self._get_param()

                # Day 5, part b
                case 5:  # Jump to second paramter if first is non-zero
                    p1, p2 = self._get_params(2)

                    if p1 != 0:
                        self.pointer = p2
                case 6:  # Jump to second paramter if first is zero
                    p1, p2 = self._get_params(2)

                    if p1 == 0:
                        self.pointer = p2
                case 7:  # Set value of 
                    p1, p2 = self._get_params(2)
                    p3 = self._read_next()

                    self.program[p3] = int(p1 < p2)
                case 8:  # Equals
                    p1, p2 = self._get_params(2)
                    p3 = self._read_next()

                    self.program[p3] = int(p1 == p2)

                # Day 2
                case 99:
                    break
                case _ as opcode:
                    raise ValueError(f"Unknown opcode: {opcode}")

        if reset:
            self.reset()

        return program_output

    def reset(self):
        self.pointer = 0
        self.program = self.initial_program.copy()
        self.current_instruction = 0

    @classmethod
    def parse_input(cls, input_string: str, *args, **kwargs):
        program = parse_numbers(input_string, include_negative=True)

        return cls(program, *args, **kwargs)
