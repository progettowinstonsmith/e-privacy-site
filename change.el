;; This buffer is for notes you don't want to save, and for Lisp evaluation.
;; If you want to create a file, visit that file with C-x C-f,
;; then enter the text in that file's own buffer.


(defun pp-accents ()
  (interactive)
  (save-excursion
    (goto-char 1)
    (query-replace-regexp "a'" "à" )
    (goto-char 1)
    (query-replace-regexp "e'" "è" )
    (goto-char 1)
    (query-replace-regexp "e'" "é" )
    (goto-char 1)
    (query-replace-regexp "i'" "ì" )
    (goto-char 1)
    (query-replace-regexp "o'" "ò" )
    (goto-char 1)
    (query-replace-regexp "u'" "ù" )
    (goto-char 1)
    (query-replace-regexp "`" "'" )
    ))


(defun pp-end ()
  (interactive)
  (save-excursion
    (goto-char 1)
    (query-replace-regexp "(?!_)  *$"  "")
  ))
  
  
  

(defun pp-lnk ()
  (interactive)
  (save-excursion   
    (goto-char 1)
    (query-replace-regexp
     "(\\(atti\\|audio\\|video\\)/"
     ")](http://urna.winstonsmith.org/materiali/2005/\\1/"
     )))

(defun pp-ppt ()
  (interactive)
  (save-excursion
    (goto-char 1)
    (query-replace-regexp
     "slide in formato \\[ppt\\]"
     "[ ![ppt]({filename}/images/icon/presentation.png)]")))

(defun pp-ogg ()
(interactive)
(goto-char 1)
(query-replace-regexp
 ",* *audio in formato \\[ *ogg\\]"
 "
[ ![ogg]({filename}/images/icon/sound.png)]"))

(defun pp-pdf ()
  (interactive)
  (save-excursion
    (goto-char 1)
    (query-replace-regexp
     "slide in formato \\[pdf\\]"
     "[ ![pdf]({filename}/images/icon/presentation.png)]")))


(defun pp-ppt ()
(interactive)
(goto-char 1)
(query-replace-regexp
 "slide in formato \\[ppt\\]"
 "[ ![ppt]({filename}/images/icon/presentation.png)]"))

(defun pp-html ()
(interactive)
(goto-char 1)
(query-replace-regexp
 "slide in formato \\[html\\]"
 "[ ![html]({filename}/images/icon/presentation.png)]"))>

(defun pp-xppt ()
(interactive)
(goto-char 1)
(query-replace-regexp
 ", \\[ppt\\]"
 "[ ![ppt]({filename}/images/icon/presentation.png)]"))

(defun pp-xooo ()
(interactive)
(goto-char 1)
(query-replace-regexp
 ", \\[ooo\\]"
 "[ ![ooo]({filename}/images/icon/document.png)]"))

(defun pp-xkpr ()
(interactive)
(goto-char 1)
(query-replace-regexp
 "[,\.] \\[kpr\\]"
 "[ ![kpr]({filename}/images/icon/presentation.png)]"))

(defun pp-xsxi ()
(interactive)
(goto-char 1)
(query-replace-regexp
 "[,\.] \\[sxi\\]"
 "[ ![sxi]({filename}/images/icon/presentation.png)]"))
