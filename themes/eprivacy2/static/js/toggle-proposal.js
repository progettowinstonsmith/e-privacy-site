document.addEventListener('DOMContentLoaded', function(){
  // se le proposte sono chiuse...
  if (window.PROPOSALS_OPEN === false) {
    // 1) nascondi il form
    var form = document.getElementById('form_wrapper_propostatalk');
    if (form) {
      form.style.display = 'none';
      // 2) inserisci un messaggio
      var msg = document.createElement('div');
      msg.className = 'proposal-closed-msg';
      msg.innerHTML = '<p>Le proposte sono al momento chiuse.</p>';
      form.parentNode.insertBefore(msg, form);
    }
  }
});
