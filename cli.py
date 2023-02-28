import argparse
import manage_contacts as mc
import templates as tm

global_parser = argparse.ArgumentParser(prog="cli")
subparsers = global_parser.add_subparsers(title="subcommands", help="contact book commands")

add_parser = subparsers.add_parser("add", help = "Add <name phone email>")
add_parser.add_argument(**tm.add_template())
add_parser.set_defaults(func=mc.insert_values)

view_parser = subparsers.add_parser("view", help = "view <all>")
view_parser.add_argument(**tm.view_template())
view_parser.set_defaults(func=mc.view_contacts)

del_parser = subparsers.add_parser("delete", help = "delete <key>")
del_parser.add_argument(**tm.del_template())
del_parser.set_defaults(func=mc.delete)

update_parser = subparsers.add_parser("update", help= "update <id field update_content>")
update_parser.add_argument(**tm.update_template())
update_parser.set_defaults(func=mc.update)


args = global_parser.parse_args()
args.func(*args.details)
