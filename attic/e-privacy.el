(require 'cl-lib)

(defcustom pws-site-directory "~/Dropbox/WORKING/PROJECTS/2024-PRJ-PWS-WORK/sites/e-privacy-site"
  "Directory root for PWS site content."
  :type 'string
  :group 'pws)

(defun arabic-to-roman (num)
  "Convert an integer NUM to a Roman numeral."
  (let ((values '(1000 900 500 400 100 90 50 40 10 9 5 4 1))
        (romans '("M" "CM" "D" "CD" "C" "XC" "L" "XL" "X" "IX" "V" "IV" "I"))
        (result ""))
    (while values
      (while (>= num (car values))
        (setq result (concat result (car romans)))
        (setq num (- num (car values))))
      (setq values (cdr values))
      (setq romans (cdr romans)))
    result))

(defun pws-compile-template-file (template-file output-file replacements)
  "Compila TEMPLATE-FILE sostituendo i placeholder in REPLACEMENTS e salva come OUTPUT-FILE."
  (with-temp-buffer
    (insert-file-contents template-file)
    (dolist (rep replacements)
      (goto-char (point-min))
      (while (re-search-forward (car rep) nil t)
        (replace-match (cdr rep) nil t)))
    (write-file output-file)))

(defun pws-create-event (year season num city where when title subtitle timeline)
  "Create event structure for PWS in the specified YEAR and SEASON."
  (interactive "nEnter Year: \nsEnter Season: \nnEnter Event Number: \nsEnter City: \nsEnter Location and Mode (e.g., 'Firenze & Streaming'): \nsEnter Dates (e.g., '16-17 maggio'): \nsEnter Title: \nsEnter Subtitle: \nsEnter Timeline (e.g., '4 marzo | 25 marzo | 29 aprile'): ")
  (let* ((work-dir (file-name-concat   pws-site-directory "content" (number-to-string year) season))
         (vars-file (file-name-concat work-dir "vars"))
         (prev-num (1- num))  ; You might want to calculate this based on `num`
         (next-num "")
	 (evt-num (arabic-to-roman num))
	 (prev-evt-num (arabic-to-roman prev-num))
         (vars-contents (format "Title: %s\nCategory: %s\nlang: it\nNum: %s\nYear: %s\nCity: %s\nWhere: %s\nWhen: %s\nSeason: %s\nSlogan: <i>\"I popoli non dovrebbero temere i propri governi: sono i governi che dovrebbero temere i propri popoli.\"</i><br/><b>V (da John Basil Barnhill)</b>\nprevid: 2023W\nprev: e-privacy-%s\nnextid:\nnext:\ntimeline: %s\ncss: .title-%s { font: 25px arial, sans-serif; text-align: center; }   .subtitle-%s { font: 18px arial, sans-serif; text-align: center; }\n"
                                 title year evt-num year city where when season prev-evt-num timeline evt-num evt-num)))
    (unless (file-exists-p work-dir)
      (make-directory work-dir t))
    (with-temp-file vars-file
      (insert vars-contents))
    (message "Event created in %s" work-dir)))



(defun pws-compile-template-files (year season num city where when title subtitle timeline)
  "Process all .template files in the templates directory, replace variables, and save them in the workdir."
  (interactive "nEnter Year: \nsEnter Season: \nnEnter Event Number: \nsEnter City: \nsEnter Location and Mode (e.g., 'Firenze & Streaming'): \nsEnter Dates (e.g., '16-17 maggio'): \nsEnter Title: \nsEnter Subtitle: \nsEnter Timeline (e.g., '4 marzo | 25 marzo | 29 aprile'): ")
  (let* ((templates-dir (file-name-concat pws-site-directory "templates"))
         (work-dir (file-name-concat pws-site-directory "content" (number-to-string year) season))
         (prev-num (1- num))  ; Assumes sequential numbering
         (evt-num (arabic-to-roman num))
         (prev-evt-num (arabic-to-roman prev-num))
	 (previd  (if (equal season "summer") (concat (number-to-string (1- year)) "W") (number-to-string year)))	 
         (vars-contents `(("Title" . ,title)
                          ("Category" . ,(number-to-string year))
                          ("lang" . "it")
                          ("Num" . ,evt-num)
                          ("Year" . ,(number-to-string year))
                          ("City" . ,city)
                          ("Where" . ,where)
                          ("When" . ,when)
                          ("Season" . ,season)
                          ("Slogan" . "<i>\"I popoli non dovrebbero temere i propri governi: sono i governi che dovrebbero temere i propri popoli.\"</i><br/><b>V (da John Basil Barnhill)</b>")
                          ("previd" . ,previd)
                          ("prev" . ,(format "e-privacy-%s" prev-evt-num))
                          ("timeline" . ,timeline)
                          ("css-title" . ,(format ".title-%s { font: 25px arial, sans-serif; text-align: center; }" evt-num))
                          ("css-subtitle" . ,(format ".subtitle-%s { font: 18px arial, sans-serif; text-align: center; }" evt-num)))))
    (unless (file-exists-p work-dir)
      (make-directory work-dir t))
    (dolist (template (directory-files templates-dir t "\\.template\\'"))
      (let ((contents (with-temp-buffer
                        (insert-file-contents template)
                        (buffer-string)))
            (output-file (concat work-dir "/" (file-name-base template))))
        (dolist (pair vars-contents)
          (setq contents (replace-regexp-in-string (format "{%s}" (car pair)) (cdr pair) contents)))
        (with-temp-file output-file
          (insert contents))))
    (message "Template files processed and saved in %s" work-dir)))
