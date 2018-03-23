# Lesson 14 - Advanced HTML

[All Lessons](https://zsiegel92.github.io/Eitan_S/)

[TOC]

## Review of [Lesson 13](https://zsiegel92.github.io/Eitan_S/Lessons/Lesson_13_HTML/Lesson13.html)

>Make sure you have completed the Khan Academy HTML-CSS basics sequence starting with [this video](https://www.khanacademy.org/computing/computer-programming/html-css/intro-to-html/p/html-basics).

Browsers send **requests** to **servers**, and servers respond by sending **HTML**, **JavaScript**, and **CSS** code to the browser. The browser then *runs* the JavaScript code, *renders* (*displays*) the HTML, and uses the CSS to *style* the HTML. **If this all sounds confusing, please review the previous lesson!**

We have seen that we can edit HTML, CSS, and Javascript, and instantly see changes in the resulting website using **Plunker**:

<iframe height="400px" width="100%" src="https://embed.plnkr.co/T3ehZ37qrg5ErRVIuz60/" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

>This embedded window is called a **plunk** from *Plunker*. Just like *repl.it* allows us to run Python code in the browser, *plnkr.co* allows us to run *browser code* in the browser.
>
>Press the <img src="fullscreen.png" width="20" alt="fullscreen"/> button to see how a page like this would be rendered in your browser.

Now, press the <img src="filetree.png" width="20" alt="file_tree"/> button to view the **file tree** in the following plunk. Notice the *Python* file `app.py`! Python *does not* run in a browser.

We **served** this website by following these steps:

1. Press the <img src="download.png" width="20" alt="download"/> button (`Project.zip` is fine).
2. Navigate to the `.zip` file and "unzip" it (by double-clicking the file). This is your project folder.
3. Open the *command prompt* and navigate into the project folder: `cd something/something/.../Downloads/Project`
4. Type `python app.py` and navigate to `127.0.0.1` *in any browser on your computer*.
	* The address may be slightly different. Look in your command prompt window for text like `* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)` and navigate to the link provided.
5. **Now you're both the *client* and the *server***.

>Make sure to get local file serving up and running before moving on!


## Serving Content

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/flask-basic?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
>It's important to know how to run code and, in particular, **serve** content from your own computer, but we will be doing most of our work on repl.it.
>
>On `repl.it`, **the server code will usually be in the file `main.py`**.

Press the Run/Play button and then click the <img src="popout.png" width="20" alt="popout"/> button (or navigate to [https://flask-basic--ZSiegel.repl.co](https://flask-basic--ZSiegel.repl.co)) to view **the served content** in your browser window, courtesy of `repl.it` making sure it makes it to us.

>This is just like what you were able to see on your browser when you executed `python app.py` and opened your browser to `http://127.0.0.1:5000/`!

Now, navigate to that same URL, with a `/goodbye` on the end ([https://flask-basic--ZSiegel.repl.co](https://flask-basic--ZSiegel.repl.co)). What do you see? How did Python generate what you see?

## Cooler Content

Early on, we used iteration in Python to create cool images. Now, we will do that in your browser.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/asterisktriangle?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
>Recall that we can *multiply* a `str` variable by an `int` to **copy** the `str` over and over again
> ```python
> >>> print("hello"*3)
> hellohellohello
> ```
>Also recall that the **special character** `"\n"` is the *newline character* that creates a line break:
> ```python
> >>> print("hello" + "\n\n" + "hello"+ "\n\n" + "hello")
> hello
>
> hello
>
> hello
> ```

Now, let's put that process in a **function** (using `def`), so that we can call it over and over (without failing the DRY principl):

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/asterisktrianglefunction?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Finally, let's SERVE our triangle using Flask:

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/asterisktriangleflaskn?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Now, the line `@app.route('/triangle')` means that **if we request our website with `/triangle` at the end of the URL** ([`https://asterisktriangleflaskn--ZSiegel.repl.co/triangle`](https://asterisktriangleflaskn--ZSiegel.repl.co/triangle)), **we will be served whatever the function `show_triangle` returns**.

>Navigate to [`.../triangle`](https://asterisktriangleflaskn--ZSiegel.repl.co/triangle). Do you see our triangle? No, just a flat row of asterisks?

In our first HTML lessons, we have seen that to create a **line break** in HTML, we use the `<br>` tag. It seems that the browser doesn't use the newline character `\n` in the same way Python does.

Let's spruce up our function to display a proper triangle by replacing `\n` with `<br>` and try to pull off the triangle in the browser.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/asterisktriangleflaskbr?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
>Now, navigating to [`.../triangle`](https://asterisktriangleflaskbr--zsiegel.repl.co/triangle) should render a full triangle!


## Content in Other Files

Flask can send a file using `app.send_static_file`, and it can also send a file that it has *rendered* (or *templated*) using `render_template`.

The `render_template` function looks for files in the `templates` directory. The `app.send_static_file` function looks for files in the `static` directory.

<iframe height="400px" width="100%" src="https://repl.it/@ZSiegel/flask-templating?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

* When we `return` the output of `app.send_static_file`, we just send whatever is in a file, as is, to the browser, which figures out what to do with it.
* When we `return` the output of `render_template`, we send whatever is in a file, but, before we send it, all the pairs of curly braces in the file (`{{something}}`) get looked at. If we give information about what `something` is, then `{{something}}` gets replaced with the value of `something`.

The line `return render_template('templated1.html', student_name="Wall-E")` does the following:

1. Finds `templated1.html` in the `templates` directory
2. Looks through `templated1.html` and notices the `{{ student_name }}` on line 15
3. Replaces `{{ student_name }}` with the value `"Wall-E"` because we called `render_template('templated1.html', student_name="Wall-E")`
4. Flask sends whatever is after `return` to anyone who visits our website with the route `/coolestpage` because of the command `@app.route('/coolestpage')` above the definition of the function `coolest_page`.

### Questions

We have a lot to explore! The upcoming topics are:

* **HTML Navigation** - Inserting links in our HTML using **anchor tags** (`<a href="http://website.com">A link!</a>`) so that we don't have to type routes into the browser
* **Routing** - determining what should be returned based on what URL a request is sent to
* **Templating** - Inserting interesting content in HTML using `render_template`


## Assignments

Fork any of the `repl.it` apps above and make ANY changes to the HTML and the Python code so that something new is displayed on screen. You can make WHATEVER changes you want, as long as the website runs.




