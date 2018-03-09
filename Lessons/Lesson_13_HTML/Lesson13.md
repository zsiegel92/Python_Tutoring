# Lesson 13 - Serving HTML

[All Lessons](https://zsiegel92.github.io/Eitan_S/)

[TOC]

## HTML - Meet Plunker!

We have mentioned that browsers (Google Chrome, Mozilla Firefox, Microsoft Edge/Internet Explorer) render webpages by reading **HTML**.

<iframe height="400px" width="100%" src="https://embed.plnkr.co/YJENImxWcIprhYBn6Ax0/" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>This embedded window is called a **plunk** from *Plunker*. Just like *repl.it* allows us to run Python code in the browser, *plnkr.co* allows us to run *browser code* in the browser.
>
>You may be thinking "but my browser *already* runs browser code!" You're right. Plunker gives us a nice little editor, though, and allows us to see changes immediately.
>
>Press the <img src="fullscreen.png" width="20" alt="fullscreen"/> button to see how a page like this would be rendered in your browser.


### "Browser Code"

Browsers run the following types of code:

* **HTML**: this tells your browser what to display. It includes the content of a webpage (text, images, etc), as well as instructions for where and how to position everything. These instructions are written so that the browser knows what to do even when a window is resized or even when a small device (like a phone) is used.
	* HTML is stored in `.html` files
* **JavaScript**: this tells your browser what to *do*. For example, a browser can run complicated code to display the correct information. This code will be written in JavaScript.
	* JavaScript is stored in `.js` files, and can also be inserted in `.html` files.
* **CSS**: this tells your browser how to format your HTML. CSS affects the font, color, position, size, and shape of elements on your page; CSS also affects the space between elements.
	* CSS is stored in `.css` files, and can also be inserted in `.html` files.

>	* **HTML** is short for **H**yper**T**ext **M**arkup **L**anguage. A *markup* language is a language that includes content as well as instructions for how to display that content.
> * **CSS** is short for **C**ascading **S**tyle **S**heets. CSS provides style instructions, and they are *cascading* in the following sense:
>		"The CSS specification describes a priority scheme to determine which style rules apply if more than one rule matches against a particular element. In this so-called cascade, priorities (or weights) are calculated and assigned to rules, so that the results are predictable." -[Wikipeida (Cascading Style Sheets)](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

## Why have we been learning Python?!

Press the <img src="filetree.png" width="20" alt="file_tree"/> button to view the **file tree** in the following plunk.


<iframe height="400px" width="100%" src="https://embed.plnkr.co/T3ehZ37qrg5ErRVIuz60/" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>A **file tree** is the folders and files that make up a project.

**The file `app.py` is a Python file! That can't run in your browser!** What's it doing there?

### Server

>"In computing, a server is a computer program or a device that provides functionality for other programs or devices, called "clients". This architecture is called the client–server model, and a single overall computation is distributed across multiple processes or devices. Servers can provide various functionalities, often called "services", such as sharing data or resources among multiple clients, or performing computation for a client." -[Wikipedia (Server)](https://en.wikipedia.org/wiki/Server_(computing))

**The code in `app.py` contains commands to **serve** the files that are being served by Plunker.** We can serve these files from any computer by running `app.py` within the filetree of this project.

Let's serve this project:

1. Press the <img src="download.png" width="20" alt="download"/> button (`Project.zip` is fine).
2. Navigate to the `.zip` file and "unzip" it (by double-clicking the file). This is your project folder.
3. Open the *command prompt* and navigate into the project folder: `cd something/something/.../Downloads/Project`
4. Type `python app.py` and navigate to `127.0.0.1` *in any browser on your computer*.
	* The address may be slightly different. Look in your command prompt window for text like `* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)` and navigate to the link provided.
5. **Now you're both the *client* and the *server***.

#### Make Changes

Simplify your `index` function from this:

```python
@app.route("/")
def index():
    return app.send_static_file('index.html')
```

to this:

```python
@app.route("/")
def index():
    return "Hello"
```

Now `app.py` should look like this:

```python
from flask import Flask

app = Flask(__name__,static_url_path='')

@app.route("/")
def index():
    return "Hello"

if __name__=="__main__":
    app.run()
```

When you navigate to the page you're serving, you should just see the text "Hello". That's because browsers can render very complex HTML, or very simple HTML with no markup instructions.

>`send_static_file` sends your browser a `.html` file, and your browser puts it on screen. If you just send text (in a `str` variable) to your browser, it will display it like it would the contents of a `.html` file.

Try editing the `.html` file like you would in Plunker and refresh your browser. The Python server framework `Flask` will serve the updated webpage.


## Assignments

**For these assignments, you will need to watch all the Khan Academy videos accompanying each lesson**.

1. Watch [this introduction to HTML video from Khan Academy](https://www.khanacademy.org/computing/computer-programming/html-css/intro-to-html/p/html-basics). If you don't have a Khan Academy account, please make one to track your progress.

2. Complete the [Khan Academy "Write a Poem" assignment](https://www.khanacademy.org/computing/computer-programming/html-css/intro-to-html/p/challenge-write-a-poem).

3. Use `<strong></strong>` and `<em></em>` tags to make text **bold** and *italicized* in [Khan Academy's "You can learn text tags" challenge](https://www.khanacademy.org/computing/computer-programming/html-css/intro-to-html/p/challenge-you-can-learn-text-tags).

4. Use `<li></li>` tags to make a list in [Khan Academy's "Your learning list" challenge](https://www.khanacademy.org/computing/computer-programming/html-css/intro-to-html/p/challenge-your-learning-list).

5. Use `<img>` tags to complete [Khan Academy's "A picture perfect trip" challenge](https://www.khanacademy.org/computing/computer-programming/html-css/intro-to-html/p/challenge-a-picture-perfect-trip).

6. Watch the [Khan Academy CSS Basics video](https://www.khanacademy.org/computing/computer-programming/html-css/intro-to-css/p/css-basics).









