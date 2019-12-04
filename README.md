# expense-tracker
A simple API for an expense tracking application along with a multiple interfaces to use it.

Watch the video here: https://youtu.be/sYBDJ15dNVc


A demonstration of programming with a database and creating an abstracted API, along with various interfaces which use it.

## Requirements
- Python
- docopt
- tabulate
- sqlite3 for desktop (helpful, but not necessary)

To install a python package use the following command:

```sh
pip install <package_name>
```

Alternatively, to install all the packages at once, use this command:
```sh
pip install -r requirements.txt
```
## Using the CLI
You can use the binary directly, in `bin/`. Add the folder to your `PATH` and then just perform an initialization to use it.

If you're using the python file,
```sh
$ python spent_driver.py init
```

If you're using the binary,
```sh
$ spent init
```
*The following examples are for using the binary. If you're using the python file, modify accordingly.*

Logging an expense:
```sh
$ spent <amount> <category> [<message>]
```
`message` is optional.

For example,
```sh
$ spent 50 food "snacks in the evening"
$ spent 100 transport
```

Viewing your expenditure:
```sh
spent_driver.py view [<view_category>]
```
For example,
```sh
$ spent view
$ spent view food
```

The first command shows you your total expenditure, along with a list of all transactions you've made.

The second one is more streamlined, and gives you the details for the sepecified category.

*An example output*
```sh
$ spent view
Total expense: 5200
----  ---------  ----------------------  --------------------------
 100  food       None                    2018-12-02 15:41:17.823609
 200  cinema     None                    2018-12-02 15:41:22.958207
 300  taxi       None                    2018-12-02 15:41:28.565593
 100  groceries  having friends over     2018-12-02 15:42:40.332875
1500  travel     air tickets to go home  2018-12-02 15:43:10.711194
3000  rent       security deposit        2018-12-02 15:44:28.739984
----  ---------  ----------------------  --------------------------
```

# Contributions

Want to contribute? Great! 

There's a list of features which can be added under Issues. If you have something totally new, even better! 

