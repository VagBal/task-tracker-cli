from task_tracker_cli.database.core import Database
from task_tracker_cli.parser.core import Parser
from task_tracker_cli.inputs.core import Add, Delete, Update, Mark, ListAll, ListDone, ListInProgress

def main():
    db = Database()
    parser = Parser()
    args = parser.parse_args()

    if args.add:
        Add().execute(db, args.add)
    elif args.delete:
        Delete().execute(db, int(args.delete))
    elif args.update:
        Update().execute(db,int(args.update[0]), args.update[1])
    elif args.mark:
        Mark().execute(db, int(args.mark[0]), args.mark[1])
    elif args.listall:
        ListAll().execute(db)
    elif args.listdone:
        ListDone().execute(db)
    elif args.listip:
        ListInProgress().execute(db)
    else:
        parser.parser.print_help()

if __name__ == "__main__":
    main()