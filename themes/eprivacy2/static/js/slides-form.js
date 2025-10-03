/* global document, sessionStorage */
(function(){
  'use strict';

  function generateChallenge() {
    var a = Math.floor(Math.random() * 9) + 1;
    var b = Math.floor(Math.random() * 9) + 1;
    return { a: a, b: b, sum: a + b };
  }

  function showError(container, message) {
    if (!container) { return; }
    container.textContent = message;
    container.style.display = message ? 'block' : 'none';
  }

  document.addEventListener('DOMContentLoaded', function(){
    var form = document.getElementById('slides-form');
    if (!form) { return; }

    var errorBox = document.getElementById('slides-error');
    var emailField = document.getElementById('slides_email');
    var select = document.getElementById('slides_submitter');
    var passwordField = document.getElementById('slides_password');
    var captchaQuestion = document.getElementById('slides_captcha_question');
    var captchaAnswer = document.getElementById('slides_captcha_answer');
    var captchaA = document.getElementById('slides_captcha_a');
    var captchaB = document.getElementById('slides_captcha_b');

    var challenge = generateChallenge();
    captchaA.value = challenge.a;
    captchaB.value = challenge.b;
    if (captchaQuestion) {
      captchaQuestion.textContent = challenge.a + ' + ' + challenge.b + ' = ?';
    }

    if (select && emailField) {
      select.addEventListener('change', function(){
        var option = select.options[select.selectedIndex];
        var preset = option ? option.getAttribute('data-email') : '';
        if (preset && !emailField.value) {
          emailField.value = preset;
        }
      });
    }

    form.addEventListener('submit', function(evt){
      showError(errorBox, '');

      if (passwordField && passwordField.value.trim() === '') {
        evt.preventDefault();
        showError(errorBox, 'Inserisci la password.');
        passwordField.focus();
        return;
      }

      var expected = challenge.sum;
      var answer = parseInt(captchaAnswer.value, 10);
      if (isNaN(answer) || answer !== expected) {
        evt.preventDefault();
        showError(errorBox, 'Il risultato del calcolo è errato.');
        captchaAnswer.focus();
        return;
      }
    });
  });
})();
