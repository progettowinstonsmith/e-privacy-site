/**
 * form-handler.js
 * Gestisce:
 *  - show/hide del campo “Altro argomento”
 *  - clonazione/removal dei relatori
 *  - sincronizzazione Email Talk → primo relatore
 *  - validazione HTML5‐style dei campi con data‐validate
 */

(function(){
  'use strict';

  // Utility di validazione
  function validateEmail(email) {
    var at = email.indexOf('@'),
        dot = email.lastIndexOf('.');
    return !(at < 1 || dot < at + 2 || dot + 2 >= email.length);
  }

  function validateOptions(elems) {
    if (!elems) return false;
    var list = (elems.length === undefined) ? [elems] : Array.prototype.slice.call(elems);
    return list.some(function(el){ return el.checked; });
  }

  function clearError(container) {
    var msg = container.querySelector('.form-errormsg');
    if (msg) msg.style.display = 'none';
    container.classList.remove('form-has-error');
  }

  function markError(container) {
    var msg = container.querySelector('.form-errormsg');
    if (msg) msg.style.display = 'block';
    container.classList.add('form-has-error');
  }

  function validateContainer(container) {
    var type = container.getAttribute('data-validation-type'),
        ok = true, inp;
    switch(type) {
      case 'email':
        inp = container.querySelector('input[type="email"]');
        ok = inp && validateEmail(inp.value.trim());
        break;
      case 'text':
        inp = container.querySelector('input[type="text"]');
        ok = inp && inp.value.trim() !== '';
        break;
      case 'textarea':
        inp = container.querySelector('textarea');
        ok = inp && inp.value.trim() !== '';
        break;
      case 'tel':
        inp = container.querySelector('input[type="tel"]');
        ok = inp && inp.value.trim() !== '';
        break;
      case 'select':
        inp = container.querySelector('select');
        ok = inp && inp.value.trim() !== '';
        break;
      case 'checkboxgrp':
        ok = validateOptions(container.querySelectorAll('input[type="checkbox"]'));
        break;
      case 'radiogrp':
        ok = validateOptions(container.querySelectorAll('input[type="radio"]'));
        break;
      default:
        ok = true;
    }
    return ok;
  }

  function validateForm(form) {
    var allValid = true,
        containers = form.querySelectorAll('[data-validate]');
    Array.prototype.forEach.call(containers, function(container){
      clearError(container);
      if (!validateContainer(container)) {
        markError(container);
        allValid = false;
      }
    });
    return allValid;
  }


  document.addEventListener('DOMContentLoaded', function(){
    var form = document.getElementById('form_propostatalk');
    if (!form) return;

    //
    // 1) Show/hide “Altro argomento”
    //
    (function(){
      var cb = document.querySelector('input[name="form[argomento__aree_di_intere1][]"][value="Altro:"]'),
          wrap = document.getElementById('form_propostatalk_quale_altro_argomento');
      if (cb && wrap) {
        cb.addEventListener('change', function(){
          wrap.style.display = cb.checked ? '' : 'none';
        });
        // iniziale
        wrap.style.display = cb.checked ? '' : 'none';
      }
    })();

    //
    // 2) Clonazione / rimozione relatori
    //
    (function(){
      var container = document.getElementById('speakers'),
          addBtn    = document.getElementById('addSpeaker'),
          remBtn    = document.getElementById('removeSpeaker');
      if (!container || !addBtn || !remBtn) return;

      function updateSummaries() {
        Array.prototype.forEach.call(container.querySelectorAll('details.speaker'), function(det, i){
          var sum = det.querySelector('summary');
          if (sum) sum.textContent = 'Relatore ' + (i+1) + ': Compila i dati';
        });
      }

      addBtn.addEventListener('click', function(){
        var orig  = container.querySelector('details.speaker'),
            clone = orig.cloneNode(true);
        clone.removeAttribute('open');
        clone.querySelectorAll('input, textarea').forEach(function(el){ el.value = ''; });
        container.appendChild(clone);
        updateSummaries();
      });

      remBtn.addEventListener('click', function(){
        var items = container.querySelectorAll('details.speaker');
        if (items.length > 1) {
          items[items.length - 1].remove();
          updateSummaries();
        }
      });
    })();

    //
    // 3) Sync Email Talk → primo relatore
    //
    (function(){
      var talkEmail = document.getElementById('form_input_propostatalk_email_di_contatto_con_il');
      if (!talkEmail) return;
      function sync(val) {
        var first = document.querySelector('#speakers .speaker input[name="form[email]"]');
        if (first) first.value = val;
      }
      sync(talkEmail.value);
      talkEmail.addEventListener('input', function(e){ sync(e.target.value); });
    })();

    //
    // 4) Validazione e apertura di tutte le <details> prima del submit
    //
    form.addEventListener('submit', function(e){
      // rendi visibili eventuali tab chiuse
      form.querySelectorAll('details.speaker').forEach(function(d){ d.setAttribute('open',''); });
      if (!validateForm(form)) {
        e.preventDefault();
        // opzionale: form.reportValidity();
      }
    });

  });

})();
