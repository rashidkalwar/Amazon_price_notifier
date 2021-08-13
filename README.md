# Amazon_price_notifier

Amazon price notifier is a cross platform desktop application that allows user to get desktop notfications when the price of their desired product drops to their target budget. This App will work on Windows, Linux, and Mac OS.

This repository requires python 3.0 or above, so make sure that is installed on your machine. Download or clone the repository and create a virtual environmen by using the following command:

```bash
 python -m venv env
```
After creating a virtual environment, install all the necessary packages by using the following command:
```bash
pip install -r requirements.txt
```
if you want you can open the `main.py` file and change the values of `url` and `target_price` variables to run the app with your given data, if not you can use it with default given data.


open your command line interface and run following command to run the app:
```bash
python main.py
```
If you using it on Mac it will open a Safari instance, it will also automatically close that so you don't need to worry about.
