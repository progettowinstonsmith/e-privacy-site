(defun pp-accents ()
  (interactive)
  (save-excursion
    (goto-char 1)
    (query-replace-regexp "`" "'" )
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
    ))


(defun pp-end ()
  (interactive)
  (save-excursion
    (goto-char 1)
    (query-replace-regexp "(?!_)  +$"  "")
  ))
  
  
(defun pp-lnk ()
  (interactive)
  (save-excursion   
    (goto-char 1)
    (query-replace-regexp
     "(\\(atti\\|audio\\|video\\)/"
    "(http://urna.winstonsmith.org/materiali/2009/\\1/"
     )))


(defun pp-mp3 ()
(interactive)
(goto-char 1)
(query-replace-regexp
 "[,;]* *audio mp3 dell' *\\[intervento\\]"
 "
[ ![mp3]({filename}/images/icon/sound.png \"MP3\")]")
(goto-char 1)
(query-replace-regexp
 "[,;]* *audio in formato *\\[ *mp3\\]"
 "
[![mp3]({filename}/images/icon/sound.png \"MP3\")]")
(query-replace-regexp
 "[,;]* *registrazione in formato *\\[ *mp3\\]"
 "
[![mp3]({filename}/images/icon/sound.png \"MP3\")]")
)

(defun pp-oggi ()
(interactive)
(goto-char 1)
(query-replace-regexp
 "[,;]* *audio ogg dell' *\\[intervento\\]"
 "
[ ![ogg]({filename}/images/icon/sound.png \"OGG\")]")
(goto-char 1)
(query-replace-regexp
 "[,;]* *audio in formato *\\[ *ogg\\]"
 "
[![mp3]({filename}/images/icon/sound.png \"OGG\")]")
)

(defun pp-ogg ()
(interactive)
(goto-char 1)
(query-replace-regexp
 ",* *audio in formato  +\\[ogg\\]"
 "
[![ogg]({filename}/images/icon/sound.png \"OGG\")]"))

(defun pp-mov ()
(interactive)
(goto-char 1)
(query-replace-regexp
 ",* *video in formato +\\[ *mov\\]"
 "
[![mov]({filename}/images/icon/sound.png \"MOV\")]"))

(defun pp-pdf ()
(interactive)
(goto-char 1)
(query-replace-regexp
 " *slides? in formato +\\[ *pdf,?\\]"
 "[![pdf]({filename}/images/icon/presentation.png)]")
(query-replace-regexp
 "[,;]? *relazione in formato +\\[ *pdf,?\\]"
 "[![pdf]({filename}/images/icon/pdf.png)]"))

(defun pp-slide ()
(interactive)
(goto-char 1)
(query-replace-regexp
 " *\\[ *slide,?\\]"
 "
[![pdf]({filename}/images/icon/presentation.png)]"))

(defun pp-xppt ()
(interactive)
(goto-char 1)
(query-replace-regexp
 ",? *\\[ *ppt\\]"
 "
[![ppt]({filename}/images/icon/presentation.png)]"))

(defun pp-xodp ()
(interactive)
(goto-char 1)
(query-replace-regexp
 ",? *\\[ *odp\\]"
 "
[![odp]({filename}/images/icon/pdf.png)]"))

(defun pp-xogg ()
(interactive)
(goto-char 1)
(query-replace-regexp
 ",? *\\[ *ogg\\]"
 "
[![ogg]({filename}/images/icon/sound.png)]"))


(defun pp-ppt ()
(interactive)
(goto-char 1)
(query-replace-regexp
 "slide in formato \\[ppt\\]"
 "
[ ![ppt]({filename}/images/icon/presentation.png)]"))

(defun pp-html ()
(interactive)
(goto-char 1)
(query-replace-regexp
 "slide in formato \\[html\\]"
 "
[ ![html]({filename}/images/icon/presentation.png)]"))>

(defun pp-xppt ()
(interactive)
(goto-char 1)
(query-replace-regexp
 ", \\[ppt\\]"
 "
[ ![ppt]({filename}/images/icon/presentation.png)]"))

(defun pp-xkpr ()
(interactive)
(goto-char 1)
(query-replace-regexp
 "[,\.] \\[kpr\\]"
 "
[ ![kpr]({filename}/images/icon/presentation.png)]"))

(defun pp-xrtf ()
(interactive)
(goto-char 1)
(query-replace-regexp
 "[,\.] \\[rtf\\]"
 "
[![rtf]({file†name}/images/icon/pdf.png)]"))

(defun pp-xsxi ()
(interactive)
(goto-char 1)
(query-replace-regexp
 "[,\.] \\[sxi\\]"
 "[ ![sxi]({filename}/images/icon/presentation.png)]"))
