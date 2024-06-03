# latex_converter
I use [Obsidian](https://obsidian.md/) to write on my [website](https://thomaspradae.github.io/). I use `$` and `$$` for writing LaTeX (the former for inline tex and the latter for display tex), but my site didn't support this right out the box, which is why I had to use [MathJax](https://www.mathjax.org/). Despite supporting `$$` for display tex, MathJax couldn't help me with my inline tex (plus using `$$` with mathjax meant my text would be black, which works for light mode but not for dark mode, and while there was probably some simple way of changing the color, where's the fun in not overcomplicating things? :) (plus what about my inline tex)). I also wanted to see my tex rendered in obsidian, which meant I had to look for some way to write in obsidian using `$` and `$$` but then have my text converted to `\\(`, `\\)`, `\\[`, `\\]`, while adding some sort of specification to not convert dollar signs when needed. The following repository is where I tested out my conversion script. The script is implemented using github actions, if u wanna see the specifics go into the github actions folder.  


