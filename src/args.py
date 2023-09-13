from argparse import ArgumentParser
from sys import argv
import sys

class arguments():
    def argsFunc():
        parser = ArgumentParser()
        parser.add_argument(
            "--current",
            "-c",
            type=str,
            help = "The path to the source code of the current version. Example: \\\\sourceR1\\dir"
        )
        parser.add_argument(
            "--update",
            "-u",
            type=str,
            help = "The path to the source code for release. Example: \\\\sourceR2\\dir"
        )
        parser.add_argument(
            "--version",
            "-v",
            type=str,
            help = "The release version. Example: R1"
        )
        parser.add_argument(
            "-n",
            "--name",
            type=str,
            nargs= "+",
            help = "The product name. Example: MISA AMIS"
        )
        parser.add_argument(
            "--output",
            "-o",
            default = "result.xlsx",
            type=str,
            help = "The location file to write the report output to (default: result.xlsx)"
        )

        argsList = []
        args = vars(parser.parse_args())
        current = args["current"]
        update = args["update"]
        version = args["version"]
        name = args["name"]
        if args["name"]: name = ' '.join(args["name"])
        output = args["output"]
        
        argsList.append(current)
        argsList.append(update)
        argsList.append(version)
        argsList.append(name)
        argsList.append(output)

        if len(argv) < 1:
            parser.print_help()
            sys.exit(1)

        if not current and not update:
            print("\nError: The path to the source code of the current and release version required!\n")
            parser.print_help()
            sys.exit(1)
        if not update:
            print("\nError: The path to the source code for release required!\n")
            parser.print_help()
            sys.exit(1)
        if not version:
            print("\nError: The release version required!\n")
            parser.print_help()
            sys.exit(1)
        if not name:
            print("\nError: The product name required!\n")
            parser.print_help()
            sys.exit(1)
        return argsList
