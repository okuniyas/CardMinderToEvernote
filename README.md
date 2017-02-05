## CardMinderToEvernote

A Python script to export namecard images of CardMinder to PDF files which are importable to Evernote.

## How to use

### Scan namecards by CardMinder

The fullname and the company name (except private name card) are used in PDF file name, so check them are correctly recognized by CardMinder.

The other information such as the divisions, e-mail, telephone number are **NOT** used this exporting, so you don't need to check if such information are recognized correctly by CardMinder. As CardMinder's scan may mistakes at many points, to focus only the full name and the company name would make your life easy. :-)

The other information will be recognized by Evernote after imported to Evernote for Evernote search.

Only namecards in the **"Inbox"** folder of CardMinder will be exported.
And namecards which are **Deleted** but are in **Deleted Folder** are **NOT** exported.

If you don't want to export same namacards again, please move the namecards to other folder or just delete them after you export namecards.

### Run CardMinderToEvernote.py script

This script creates a folder of today named by yyyyMMdd format.

Then generates a PDF file for each namecard in "Inbox" folder with {company name}_{fullname}.pdf format.

If there is a back image of the namecard, the generated PDF file contains two pages with the face image and the back image.

### Import to Evernote

Open the **Import folder...** panel by [Tool] - [Import folder...] of Evernote client.
Then [Add] your folder, for example;

+ Folder : Your folder path ended yyyyMMdd such as %HOME%/Desktop/CardMinderToEvernote/20170205
+ Sub folder : NO
+ Notebook : Inbox
    - I recommend that you check imported Notes in Inbox first then you move them in your Notebook for your Business Cards.
+ Source : Delete
    - You can keep PDF files local but I delete them after Evernote successly imported them.

### Move namecards in Inbox folder of CardMinder to other folder

For the next time you scan and export your namecards, move namecards to other folder than Inbox or just delete them to avoid duplicated exports.

## Why

Evernote is easy to use at any devices such as PC, Tablet and Smartphone.
and we can rely on Evernote to search namecards in details.

## Instration

### Install Python

- download Python (3.6+) from https://www.python.org/

- install and setup

### install PyPDF2 module

> pip install pypdf2

### locate CardMinderToEvernote.py

For example; create a folder at your desktop.

`%HOME%\Desktop\CardMinderToEvernote\`
  
Then put CardMinderToEvernote.py in above folder.

### Run CardMinderToEvernote.py

- Right click on CardMinderToEvernote.py file, then select [Edit with IDLE].
  
- Check if CardMinder folder is correct.

``
    source_directory = os.environ["HOME"] + "/Documents/CardMinder/CardMinder DB.cxdb/Images/"
    connection = sqlite3.connect(os.environ["HOME"] + "/Documents/CardMinder/CardMinder DB.cxdb/CardMinder1.sqldb")
``

- Check if the folder to place generated PDF files are correct.

``
    destination_directory = os.environ["HOME"] + "/Desktop/CardMinderToEvernote/" + today
``

- Run by [Run]-[Run Module (F5)]

Check if any errors displayed.

### Check exported PDF files.

Go %HOME%/Desktop/CardMinderToEvernote 's sub folder named today.
There will be PDF files for each namecards.

## Contributors and References

This script has been extented below points from the original script.

- ignore **Deleted** namecards
- select only namecards in the **Inbox** folder.
- export not only the face image but also the back image into one PDF file.

[Original](https://marvelph.wordpress.com/2011/01/23/scansnap%E4%BB%98%E5%B1%9E%E3%81%AEcardminder%E3%81%AB%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%82%93%E3%81%A0%E5%90%8D%E5%88%BA%E3%82%92evernote%E3%81%AB%E6%B5%81%E3%81%97%E8%BE%BC%E3%82%80/)

## License

[MIT](http://opensource.org/licenses/mit-license.php)

## Author

[okuniyas](https://github.com/okuniyas)
