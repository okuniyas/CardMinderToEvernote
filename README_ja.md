## CardMinderToEvernote

CardMinder の名刺データから PDFファイルを生成し、Evernoteへインポートを助けるPythonスクリプトです。

## 使い方

### 名刺を CardMinder でスキャンする

「会社名」と「氏名」のみを使います。個人で作成した名刺の場合には、「会社名」がなくてもかまいません。CardMinder上で、これらの情報が正しいことをチェックしてください。

「会社名」と「氏名」以外の情報、例えば部署名、住所、E-Mailアドレス、電話番号などは間違っていてもかまいません。CardMinderの文字認識には間違いが少なからず出ますが、 「会社名」と「氏名」だけを気にすることで、修正がだいぶ楽になります。

「会社名」と「氏名」以外の情報は、EvernoteにPDFファイルとしてインポートすることで、EvernoteのOCRに任せます。

CardMinderの**"Inbox"**フォルダにある名刺だけをエクスポートします。
さらに、**削除**した（削除済フォルダーに移動した）名刺も**対象外**とします。

エキスポートした名刺を再度エキスポートしないように、Inboxフォルダーから移動したり、削除するようにしてください。

### CardMinderToEvernote.py スクリプトを実行する

このスクリプトはまず、PDFファイルを生成するフォルダーを作成します。日付 yyyymmdd 形式のフォルダーです。

そして、"Inbox"フォルダーの名刺1枚ごとに、1つのPDFファイルを生成します。PDFファイル名は、{会社名}_{氏名}.pdf 形式です。

名刺に裏面のイメージがあれば、PDFファイルに表面と裏面の2ページを生成します。

### Evernoteでのインポート

**インポートフォルダ...** パネルを、Evernoteクライアントの[ツール] - [インポートフォルダ...] から開きます。
初めての場合、[追加] ボタンでフォルダを設定します。2回目からは、[フォルダ]を今日の日付に変更します。

+ フォルダ : PDFファイルが入ったフォルダを指定します。
    - 例えば %HOME%/Desktop/CardMinderToEvernote/20170205
+ サブフォルダ : いいえ
+ ノートブック : Inbox
    - まず、EvernoteのInboxノートブックでインポートしたノートを確認してください。それから、これらのノートをまとめて選択し、名刺用のノートブックに移動することを推奨します。
+ ソース : 削除
    - PDFファイルを残しておくこともできますが、私はインポートが成功したらEvernoteに消させています。もしEvernoteへのインポートが途中で失敗しても、成功したファイル分は消えているのでチェックが楽です。

### CardMinder上で、エクスポート済の名刺を移動する

次の名刺スキャンとエクスポートのために、名刺を別のフォルダーに移動するか、削除します。
私の場合はCardMinder上での運用をしていないので、単に削除しています。

## なぜこのようなことをするか

CardMinderは、PC上での利用に制限されます。Evernoteに置くことで、PC、タブレット、スマートフォンなど多数のデバイスで利用できるようになります。
また、Evernoteにすることで細かい情報の検索をEvernoteのOCRに任せることができます。

## インストール

### Pythonのインストール

- Python (3.6以上) を https://www.python.org/ からダウンロードします

- インストールして設定します

### PyPDF2 モジュールのインストール

> pip install pypdf2

PDFファイルのマージのためにこのモジュールを使っています。

### CardMinderToEvernote.py の保存

作業フォルダ、例えば、デスクトップに CardMinderToEvernote フォルダを作成します。

`%HOME%\Desktop\CardMinderToEvernote\`
  
そのフォルダに CardMinderToEvernote.py を置きます。

### CardMinderToEvernote.py を修正、実行する

- CardMinderToEvernote.py ファイルを右クリックし、[Edit with IDLE] を選択します。
  
- CardMinderの導入先が正しいか確認します

``
    source_directory = os.environ["HOME"] + "/Documents/CardMinder/CardMinder DB.cxdb/Images/"
    connection = sqlite3.connect(os.environ["HOME"] + "/Documents/CardMinder/CardMinder DB.cxdb/CardMinder1.sqldb")
``

必要な修正をしてください。

- 作業フォルダが正しいか確認します

``
    destination_directory = os.environ["HOME"] + "/Desktop/CardMinderToEvernote/" + today
``

- [Run]-[Run Module (F5)]から実行します

エラーが起きないか、確認します。

### 生成されたPDFファイルを確認します

%HOME%/Desktop/CardMinderToEvernote の下にある日付のサブフォルダを開きます。
名刺ごとにPDFファイルが生成されているはずです。

## 参考、および、貢献

このスクリプトは、以下のオリジナルへ、いくつかの拡張をしたものです。

- CardMinder上で**削除**された名刺を対象外とする。
- CardMinderの**Inbox**フォルダの名刺のみを対象とする。
- 表面だけでなく、裏面も含めてPDFファイルに生成する。

[オリジナル](https://marvelph.wordpress.com/2011/01/23/scansnap%E4%BB%98%E5%B1%9E%E3%81%AEcardminder%E3%81%AB%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%82%93%E3%81%A0%E5%90%8D%E5%88%BA%E3%82%92evernote%E3%81%AB%E6%B5%81%E3%81%97%E8%BE%BC%E3%82%80/)

## ライセンス

[MIT](http://opensource.org/licenses/mit-license.php)

## 作者

[okuniyas](https://github.com/okuniyas)
