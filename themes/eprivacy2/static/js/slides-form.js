/* global document */
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
    var submitterField = document.getElementById('slides_submitter');
    var emailField = document.getElementById('slides_email');
    var passwordField = document.getElementById('slides_password');
    var dayField = document.getElementById('slides_day');
    var sessionField = document.getElementById('slides_session');
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

    if (submitterField) {
      submitterField.addEventListener('input', function(){
        var value = submitterField.value || '';
        var normalised = value.normalize('NFKD').replace(/[^A-Za-z]/g, '_');
        normalised = normalised.replace(/_+/g, '_');
        normalised = normalised.replace(/^_+/, '').replace(/_+$/, '');
        normalised = normalised.slice(0, 12);
        normalised = normalised.toLowerCase();
        submitterField.value = normalised;
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

      if (dayField && !dayField.value) {
        evt.preventDefault();
        showError(errorBox, 'Seleziona la giornata.');
        dayField.focus();
        return;
      }

      if (sessionField && !sessionField.value) {
        evt.preventDefault();
        showError(errorBox, 'Seleziona la sessione.');
        sessionField.focus();
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
