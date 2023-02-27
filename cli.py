import argparse
import manage_contacts as mc

global_parser = argparse.ArgumentParser(prog="cli")
subparsers = global_parser.add_subparsers(title="subcommands", help="contact book commands")

template_1 = {
    "dest": "details",
    "type": str,
    "nargs": 3,
    "metavar": "contact details",
    "help": "string value",
}
add_parser = subparsers.add_parser("add", help = "Add contact")
add_parser.add_argument(**template_1)
add_parser.set_defaults(func=add)
args = global_parser.parse_args()

print(args)

print(args.func(*args.details))
