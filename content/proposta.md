Slug: e-privacy-proposta-talk
Category: 2025
City: Firenze
Css: .title-XXXVII { font: 25px arial, sans-serif; text-align: center; }   .subtitle-XXXVII { font: 18px arial, sans-serif; text-align: center; }
Date: 23/01/2025
Edition: winter
Enabled: yes
Eprivacy_N: XXXVII
Event_Path: content/2025/winter
Extra-Documents: nil
Giorni: 23 e 24 ottobre 2025
Lang: it
Location: Firenze
Next: 
Nextid: 
Num: XXXVII
Options: toc:nil
Prev: e-privacy-XXXVI
Previd: 2025
Season: winter
XStatus: hidden
Subtitle: TBA
Timeline: 28 marzo | 7 aprile | 12 maggio
Title: Misurare l’Umano? Dal Vitruviano all’Algoritmo
When: 23-24 ottobre
Where: TBA
Year: 2025
Template: form

<div id="form_wrapper_propostatalk" class="form_wrapper">
    <form autocomplete="false" role="form" method="post" action="/cgi-bin/submit-propostatalk.py" id="form_propostatalk" data--form="propostatalk" enctype="multipart/form-data">
    
        <div class="form-error" id="form_propostatalk_error"></div>
        <div class="form-message" id="form_propostatalk_message"></div>


        <div class="form-innerform">            
          <div class="form-page-wrapper form-page-1" data--form-page="1">
	  
            <div id="form_propostatalk_email_di_contatto_con_il" data-validate="email_di_contatto_con_il" data-validation-type="email" class="form-row form-email form-field-1 form-required">
                <label id="form_label_propostatalk_email_di_contatto_con_il" for="form_input_propostatalk_email_di_contatto_con_il" class="form-label">Email di contatto con il relatore (Identificativo del TALK)</label>
                <span class="form-helpmessage">Inserire qui un indirizzo valido di posta elettronica (questa EMAIL sarà usata come identificazione del talk nel form dei curriculum degli autori). Indicate ovviamente sempre la stessa come identificativo del TALK. Se presentate più di un talk dovete indicare una mail diversa per ogni talk, oppure mail sinonime ma differenti: ad esempio, sapete che nelle email di GMail potete aggiungere punti al nome utente a vostro piacimento? ovvero paolino.paperino@gmail.com e paolinopaperino@gmail.com sono la stessa cosa).</span>
                <input id="form_input_propostatalk_email_di_contatto_con_il" name="form[email_di_contatto_con_il]" value="" class="form-input" type="email">
                <span class="form-errormsg" style="display: none;">Su, non perdere tempo. Questo campo è obbligatorio.</span>
            </div>

            <div id="form_propostatalk_nome_e_cognome" data-validate="nome_e_cognome" data-validation-type="text" class="form-row form-text form-field-2 form-required">
                <label id="form_label_propostatalk_nome_e_cognome" for="form_input_propostatalk_nome_e_cognome" class="form-label">Nome e Cognome</label>
                <span class="form-helpmessage">Inserisci il cognome del SINGOLO relatore che terrà i contatti con l'organizzazione</span>
                <input id="form_input_propostatalk_nome_e_cognome" name="form[nome_e_cognome]" value="" class="form-input" type="text">
                <span class="form-errormsg" style="display: none;">Questo è obbligatorio</span>
            </div>

            <div id="form_propostatalk_contatto_telefonico" data-validate="contatto_telefonico" data-validation-type="tel" class="form-row form-tel form-field-3 form-required">
                <label id="form_label_propostatalk_contatto_telefonico" for="form_input_propostatalk_contatto_telefonico" class="form-label">Numero di telefono per contattare il relatore principale</label>
                <span class="form-helpmessage">Inserire qui il numero di cellulare</span>
                <input id="form_input_propostatalk_contatto_telefonico" name="form[contatto_telefonico]" value="" class="form-input" type="tel">
                <span class="form-errormsg" style="display: none;">Abbiamo bisogno di un telefono per contattarti</span>
            </div>

            <div id="form_propostatalk_proposta_di_durata" data-validate="proposta_di_durata" data-validation-type="select" class="form-row form-select form-field-4 form-required">
                <label id="form_label_propostatalk_proposta_di_durata" for="form_input_propostatalk_proposta_di_durata" class="form-label">Proposta di durata</label>
                <span class="form-helpmessage">Durata del talk comprensivo del Q&amp;A (i tempi saranno decisi dagli organizzatori in fase di costruzione del calendario, L'indicazione qui presente è solo indicativa)</span>
                <select id="form_input_propostatalk_proposta_di_durata" name="form[proposta_di_durata]" value="" class="form-selectbox">                    <option value=""></option>                    <option value="20 (meglio)">20</option>                    <option value="30 (ok)">30</option>                    <option value="45 (casi eccezionali da concordare con gli organizzatori)">45</option>
                </select>
                <span class="form-errormsg" style="display: none;">Su, non perdere tempo. Questo campo è obbligatorio.</span>
            </div>

            <div id="form_propostatalk_titolo" data-validate="titolo" data-validation-type="text" class="form-row form-text form-field-5 form-required">
                <label id="form_label_propostatalk_titolo" for="form_input_propostatalk_titolo" class="form-label">Titolo</label>
                <input id="form_input_propostatalk_titolo" name="form[titolo]" value="" class="form-input" type="text">
                <span class="form-errormsg" style="display: none;">Scrivi qualcosa</span>
            </div>

            <div id="form_propostatalk_descrizione" data-validate="descrizione" data-validation-type="textarea" class="form-row form-text form-field-6 form-required">
                <label id="form_label_propostatalk_descrizione" for="form_input_propostatalk_descrizione" class="form-label">Descrizione</label>
                <span class="form-helpmessage">Inserire una descrizione (almeno 400 caratteri) sul contenuto della relazione</span>
                <textarea id="form_input_propostatalk_descrizione" name="form[descrizione]" class="form-textarea"></textarea>
                <span class="form-errormsg" style="display: none;">Su, non perdere tempo. Questo campo è obbligatorio.</span>
            </div>

            <div id="form_propostatalk_sessioni" data-validate="sessioni" data-validation-type="checkboxgrp" class="form-row form-checkboxgrp form-field-7 form-required">
                <label class="form-label" for="form_checkboxgrp_checkbox_sessioni_PrimogiornoMattina1">Sessioni</label>
                <span class="form-helpmessage">Quando potresti essere presente (scegline anche più di una)</span>
                <div class="form-checkboxgrp-row">                    <input class="form-checkboxgrp-checkbox" name="form[sessioni][]" id="form_checkboxgrp_checkbox_sessioni_1GM0" type="checkbox" value="1GM">
                    <label id="form_checkboxgrp_label_sessioni_1GM0" for="form_checkboxgrp_checkbox_sessioni_1GM0" class="form-checkboxgrp-label">Primo giorno - Mattina</label>
                </div>
                <div class="form-checkboxgrp-row">                    <input class="form-checkboxgrp-checkbox" name="form[sessioni][]" id="form_checkboxgrp_checkbox_sessioni_1GP1" type="checkbox" value="1GP">
                    <label id="form_checkboxgrp_label_sessioni_1GP1" for="form_checkboxgrp_checkbox_sessioni_1GP1" class="form-checkboxgrp-label">Primo giorno - Pomeriggio</label>
                </div>
                <div class="form-checkboxgrp-row">                    <input class="form-checkboxgrp-checkbox" name="form[sessioni][]" id="form_checkboxgrp_checkbox_sessioni_2GM2" type="checkbox" value="2GM">
                    <label id="form_checkboxgrp_label_sessioni_2GM2" for="form_checkboxgrp_checkbox_sessioni_2GM2" class="form-checkboxgrp-label">Secondo giorno - Mattina</label>
                </div>
                <div class="form-checkboxgrp-row">                    <input class="form-checkboxgrp-checkbox" name="form[sessioni][]" id="form_checkboxgrp_checkbox_sessioni_2GP3" type="checkbox" value="2GP">
                    <label id="form_checkboxgrp_label_sessioni_2GP3" for="form_checkboxgrp_checkbox_sessioni_2GP3" class="form-checkboxgrp-label">Secondo giorno - Pomeriggio (non ancora previsto)</label>
                </div>
                <span class="form-errormsg" style="display: none;">Scegli comunque per favore, anche tutte</span>
            </div>

            <div id="form_propostatalk_dal_vivo" class="form-row form-radiogrp form-field-8">
                <label class="form-label" for="form_radiogrp_radio_dal_vivo_Farodituttoperesserci1">Dal vivo</label>
                <span class="form-helpmessage">L'evento sarà organizzato anche in presenza. Sarai presente?</span>
                <div class="form-radiogrp-row">                    <input name="form[dal_vivo]" class="form-radiogrp-radio" id="form_radiogrp_radio_dal_vivo_SI0" type="radio" value="SI+">
                    <label id="form_radiogrp_label_dal_vivo_SI0" for="form_radiogrp_radio_dal_vivo_SI0" class="form-radiogrp-label">Farò di tutto per esserci</label>
                </div>
                <div class="form-radiogrp-row">                    <input name="form[dal_vivo]" class="form-radiogrp-radio" id="form_radiogrp_radio_dal_vivo_SI1" type="radio" value="SI">
                    <label id="form_radiogrp_label_dal_vivo_SI1" for="form_radiogrp_radio_dal_vivo_SI1" class="form-radiogrp-label">Probabilmente sì</label>
                </div>
                <div class="form-radiogrp-row">                    <input name="form[dal_vivo]" class="form-radiogrp-radio" id="form_radiogrp_radio_dal_vivo_NO2" type="radio" value="NO">
                    <label id="form_radiogrp_label_dal_vivo_NO2" for="form_radiogrp_radio_dal_vivo_NO2" class="form-radiogrp-label">Probabilmente no</label>
                </div>
                <div class="form-radiogrp-row">                    <input name="form[dal_vivo]" class="form-radiogrp-radio" id="form_radiogrp_radio_dal_vivo_NO3" type="radio" value="NO+">
                    <label id="form_radiogrp_label_dal_vivo_NO3" for="form_radiogrp_radio_dal_vivo_NO3" class="form-radiogrp-label">Lo escludo</label>
                </div>
                <span class="form-errormsg" style="display: none;"></span>
            </div>

            <div id="form_propostatalk_argomento__aree_di_intere1" data-validate="argomento__aree_di_intere1" data-validation-type="checkboxgrp" class="form-row form-checkboxgrp form-field-9 form-required">
                <label class="form-label" for="form_checkboxgrp_checkbox_argomento__aree_di_intere1_Privacy1">Argomento / Aree di interesse</label>
                <span class="form-helpmessage">Inserire uno o più argomenti trattati dalla relazione</span>
                <div class="form-checkboxgrp-row">                    <input class="form-checkboxgrp-checkbox" name="form[argomento__aree_di_intere1][]" id="form_checkboxgrp_checkbox_argomento__aree_di_intere1_Privacy0" type="checkbox" value="Privacy">
                    <label id="form_checkboxgrp_label_argomento__aree_di_intere1_Privacy0" for="form_checkboxgrp_checkbox_argomento__aree_di_intere1_Privacy0" class="form-checkboxgrp-label">Privacy</label>
                </div>
                <div class="form-checkboxgrp-row">                    <input class="form-checkboxgrp-checkbox" name="form[argomento__aree_di_intere1][]" id="form_checkboxgrp_checkbox_argomento__aree_di_intere1_Anonimato1" type="checkbox" value="Anonimato">
                    <label id="form_checkboxgrp_label_argomento__aree_di_intere1_Anonimato1" for="form_checkboxgrp_checkbox_argomento__aree_di_intere1_Anonimato1" class="form-checkboxgrp-label">Anonimato</label>
                </div>
                <div class="form-checkboxgrp-row">                    <input class="form-checkboxgrp-checkbox" name="form[argomento__aree_di_intere1][]" id="form_checkboxgrp_checkbox_argomento__aree_di_intere1_DirittoallaConoscenza2" type="checkbox" value="Diritto alla Conoscenza">
                    <label id="form_checkboxgrp_label_argomento__aree_di_intere1_DirittoallaConoscenza2" for="form_checkboxgrp_checkbox_argomento__aree_di_intere1_DirittoallaConoscenza2" class="form-checkboxgrp-label">Diritto alla Conoscenza</label>
                </div>
                <div class="form-checkboxgrp-row">                    <input class="form-checkboxgrp-checkbox" name="form[argomento__aree_di_intere1][]" id="form_checkboxgrp_checkbox_argomento__aree_di_intere1_Whistleblowing3" type="checkbox" value="Whistleblowing">
                    <label id="form_checkboxgrp_label_argomento__aree_di_intere1_Whistleblowing3" for="form_checkboxgrp_checkbox_argomento__aree_di_intere1_Whistleblowing3" class="form-checkboxgrp-label">Whistleblowing</label>
                </div>
                <div class="form-checkboxgrp-row">                    <input class="form-checkboxgrp-checkbox" name="form[argomento__aree_di_intere1][]" id="form_checkboxgrp_checkbox_argomento__aree_di_intere1_eGovernment4" type="checkbox" value="eGovernment">
                    <label id="form_checkboxgrp_label_argomento__aree_di_intere1_eGovernment4" for="form_checkboxgrp_checkbox_argomento__aree_di_intere1_eGovernment4" class="form-checkboxgrp-label">eGovernment</label>
                </div>
                <div class="form-checkboxgrp-row">                    <input class="form-checkboxgrp-checkbox" name="form[argomento__aree_di_intere1][]" id="form_checkboxgrp_checkbox_argomento__aree_di_intere1_eDemocracy5" type="checkbox" value="eDemocracy">
                    <label id="form_checkboxgrp_label_argomento__aree_di_intere1_eDemocracy5" for="form_checkboxgrp_checkbox_argomento__aree_di_intere1_eDemocracy5" class="form-checkboxgrp-label">eDemocracy</label>
                </div>
                <div class="form-checkboxgrp-row">                    <input class="form-checkboxgrp-checkbox" name="form[argomento__aree_di_intere1][]" id="form_checkboxgrp_checkbox_argomento__aree_di_intere1_Tecnocontrollo6" type="checkbox" value="Tecnocontrollo">
                    <label id="form_checkboxgrp_label_argomento__aree_di_intere1_Tecnocontrollo6" for="form_checkboxgrp_checkbox_argomento__aree_di_intere1_Tecnocontrollo6" class="form-checkboxgrp-label">Tecnocontrollo</label>
                </div>
                <div class="form-checkboxgrp-row">                    <input class="form-checkboxgrp-checkbox" name="form[argomento__aree_di_intere1][]" id="form_checkboxgrp_checkbox_argomento__aree_di_intere1_PubblicaAmministrazione7" type="checkbox" value="Pubblica Amministrazione">
                    <label id="form_checkboxgrp_label_argomento__aree_di_intere1_PubblicaAmministrazione7"
		           for="form_checkboxgrp_checkbox_argomento__aree_di_intere1_PubblicaAmministrazione7"
 			   class="form-checkboxgrp-label">Pubblica Amministrazione</label>
                </div>
                <div class="form-checkboxgrp-row">                    <input class="form-checkboxgrp-checkbox" name="form[argomento__aree_di_intere1][]" id="form_checkboxgrp_checkbox_argomento__aree_di_intere1_Altro8" type="checkbox" value="Altro:">
                    <label id="form_checkboxgrp_label_argomento__aree_di_intere1_Altro8" for="form_checkboxgrp_checkbox_argomento__aree_di_intere1_Altro8" class="form-checkboxgrp-label">Altro:</label>
                </div>
                <span class="form-errormsg" style="display: none;">Su, non perdere tempo. Questo campo è obbligatorio. Scegline almeno uno</span>
            </div>

            <div id="form_propostatalk_quale_altro_argomento" data--form-show-on="argomento__aree_di_intere1:Altro:" data--form-expr="in" class="form-row form-text form-field-9  form-field-hidden">
                <label id="form_label_propostatalk_quale_altro_argomento" for="form_input_propostatalk_quale_altro_argomento" class="form-label">Quale altro argomento?</label>
                <span class="form-helpmessage">Indica qui un argomento alternativo</span>
                <input id="form_input_propostatalk_quale_altro_argomento"
		name="form[quale_altro_argomento]" value="" class="form-input" type="text">
                <span class="form-errormsg" style="display: none;"></span>
            </div>

            <div id="form_propostatalk_saranno_presenti_piu_rela" data-validate="saranno_presenti_piu_rela" data-validation-type="radiogrp" class="form-row form-radiogrp form-field-10 form-required">
                <label class="form-label" for="form_radiogrp_radio_saranno_presenti_piu_rela_Nosolouno1">Saranno presenti più relatori sul palco?</label>
                <div class="form-radiogrp-row">                    <input name="form[saranno_presenti_piu_rela]" class="form-radiogrp-radio" checked id="form_radiogrp_radio_saranno_presenti_piu_rela_No0" type="radio" value="No">
                    <label id="form_radiogrp_label_saranno_presenti_piu_rela_No0" for="form_radiogrp_radio_saranno_presenti_piu_rela_No0" class="form-radiogrp-label">No solo uno</label>
                </div>
                <div class="form-radiogrp-row">                    <input name="form[saranno_presenti_piu_rela]" class="form-radiogrp-radio" id="form_radiogrp_radio_saranno_presenti_piu_rela_Si1" type="radio" value="Si">
                    <label id="form_radiogrp_label_saranno_presenti_piu_rela_Si1" for="form_radiogrp_radio_saranno_presenti_piu_rela_Si1" class="form-radiogrp-label">Più di un relatore</label>
                </div>
                <span class="form-errormsg" style="display: none;">Su, non perdere tempo. Questo campo è obbligatorio.</span>
            </div>

            <div id="form_propostatalk_consenso_alla_pubblicazio" data-validate="consenso_alla_pubblicazio" data-validation-type="radiogrp" class="form-row form-radiogrp form-field-11 form-required">
                <label class="form-label" for="form_radiogrp_radio_consenso_alla_pubblicazio_Si1">Consenso alla pubblicazione degli atti e pubblicazione sotto licenza libera</label>
                <span class="form-helpmessage">Eventuali eccezioni alla distribuzione pubblica del materiale  vanno discusse direttamente con gli organizzatori</span>
                <div class="form-radiogrp-row">                    <input name="form[consenso_alla_pubblicazio]" class="form-radiogrp-radio" checked id="form_radiogrp_radio_consenso_alla_pubblicazio_Si0" type="radio" value="Si">
                    <label id="form_radiogrp_label_consenso_alla_pubblicazio_Si0" for="form_radiogrp_radio_consenso_alla_pubblicazio_Si0" class="form-radiogrp-label">Si</label>
                </div>
                <div class="form-radiogrp-row">                    <input name="form[consenso_alla_pubblicazio]" class="form-radiogrp-radio" id="form_radiogrp_radio_consenso_alla_pubblicazio_Nosoloconilconsensodegliorganizzatori1" type="radio" value="No* (solo con il consenso degli organizzatori)">
                    <label id="form_radiogrp_label_consenso_alla_pubblicazio_Nosoloconilconsensodegliorganizzatori1" for="form_radiogrp_radio_consenso_alla_pubblicazio_Nosoloconilconsensodegliorganizzatori1" class="form-radiogrp-label">No</label>
                </div>
                <span class="form-errormsg" style="display: none;">Su, non perdere tempo. Questo campo è obbligatorio.</span>
            </div>

            <div id="form_propostatalk_consenso_alle_registrazio" data-validate="consenso_alle_registrazio" data-validation-type="radiogrp" class="form-row form-radiogrp form-field-12 form-required">
                <label class="form-label" for="form_radiogrp_radio_consenso_alle_registrazio_Si1">Consenso alle registrazioni audio/video e pubblicazione sotto licenza libera</label>
                <span class="form-helpmessage">Eventuali eccezioni alle registrazioni del materiale  vanno discusse direttamente con gli organizzatori</span>
                <div class="form-radiogrp-row">                    <input name="form[consenso_alle_registrazio]" class="form-radiogrp-radio" checked id="form_radiogrp_radio_consenso_alle_registrazio_Si0" type="radio" value="Si">
                    <label id="form_radiogrp_label_consenso_alle_registrazio_Si0" for="form_radiogrp_radio_consenso_alle_registrazio_Si0" class="form-radiogrp-label">Si</label>
                </div>
                <div class="form-radiogrp-row">                    <input name="form[consenso_alle_registrazio]" class="form-radiogrp-radio" id="form_radiogrp_radio_consenso_alle_registrazio_No1" type="radio" value="No">
                    <label id="form_radiogrp_label_consenso_alle_registrazio_No1" for="form_radiogrp_radio_consenso_alle_registrazio_No1" class="form-radiogrp-label">No</label>
                </div>
                <span class="form-errormsg" style="display: none;">Su, non perdere tempo. Questo campo è obbligatorio.</span>
            </div>

            <div id="form_propostatalk_commenti_e_istruzioni" class="form-row form-text form-field-13">
                <label id="form_label_propostatalk_commenti_e_istruzioni" for="form_input_propostatalk_commenti_e_istruzioni" class="form-label">Eventuali commenti per gli organizzatori</label>
                <span class="form-helpmessage">Se vuoi  fare dei commenti questo è il posto giusto</span>
                <textarea id="form_input_propostatalk_commenti_e_istruzioni" name="form[commenti_e_istruzioni]" class="form-textarea"></textarea>
                <span class="form-errormsg" style="display: none;"></span>
            </div>



       <div id="speakers">
       <details open class="speaker">
        <summary>Relatore 1: Compila i dati</summary>
	<div class="speaker-fields">
 	     <h3 id="form_label_propostarelatore_identificazione_dei_relat" for="form_input_propostarelatore_identificazione_dei_relat" class="form-label">
                    Identificazione dei Relatori
            </h3>


            <div id="form_propostarelatore_cognome" data-validate="cognome" data-validation-type="text" class="form-row form-text form-field-4 form-required">
                <label id="form_label_propostarelatore_cognome" for="form_input_propostarelatore_cognome" class="form-label">Cognome</label>
                <input id="form_input_propostarelatore_cognome" name="form[cognome]" value="" class="form-input" type="text">
                <span class="form-errormsg" style="display: none;">Su, non perdere tempo. Questo campo è obbligatorio.</span>
            </div>

            <div id="form_propostarelatore_nome" data-validate="nome" data-validation-type="text" class="form-row form-text form-field-5 form-required">
                <label id="form_label_propostarelatore_nome" for="form_input_propostarelatore_nome" class="form-label">Nome</label>
                <input id="form_input_propostarelatore_nome" name="form[nome]" value="" class="form-input" type="text">
                <span class="form-errormsg" style="display: none;">Su, non perdere tempo. Questo campo è obbligatorio.</span>
            </div>

            <div id="form_propostarelatore_organizzazione_o_istituzi" class="form-row form-text form-field-6">
                <label id="form_label_propostarelatore_organizzazione_o_istituzi" for="form_input_propostarelatore_organizzazione_o_istituzi" class="form-label">Organizzazione o Istituzione</label>
                <input id="form_input_propostarelatore_organizzazione_o_istituzi" name="form[organizzazione_o_istituzi]" value="" class="form-input" type="text">
                <span class="form-errormsg" style="display: none;"></span>
            </div>

            <div id="form_propostarelatore_email" data-validate="email" data-validation-type="email" class="form-row form-email form-field-7 form-required">
                <label id="form_label_propostarelatore_email" for="form_input_propostarelatore_email" class="form-label">Email</label>
                <span class="form-helpmessage">Se il relatore del talk è uno solo qui andrà ripetuta l'email identificativa</span>
                <input id="form_input_propostarelatore_email" name="form[email]" value="" class="form-input" type="email">
                <span class="form-errormsg" style="display: none;">Questo è obbligatorio</span>
            </div>

            <div id="form_propostarelatore_numero_di_telefono" data-validate="numero_di_telefono" data-validation-type="tel" class="form-row form-tel form-field-8 form-required">
                <label id="form_label_propostarelatore_numero_di_telefono" for="form_input_propostarelatore_numero_di_telefono" class="form-label">Numero di Telefono</label>
                <span class="form-helpmessage">Il numero di telefono è importante per eventuali richieste urgenti (sarà usato solo per questo)</span>
                <input id="form_input_propostarelatore_numero_di_telefono" name="form[numero_di_telefono]" value="" class="form-input" type="tel">
                <span class="form-errormsg" style="display: none;">Abbiamo bisogno di un telefono per contattarti</span>
            </div>

            <div id="form_propostarelatore_breve_ma_non_troppo_prese" data-validate="breve_ma_non_troppo_prese" data-validation-type="textarea" class="form-row form-text form-field-9 form-required">
                <label id="form_label_propostarelatore_breve_ma_non_troppo_prese" for="form_input_propostarelatore_breve_ma_non_troppo_prese" class="form-label">Breve (ma non troppo) presentazione dell'autore.</label>
                <span class="form-helpmessage">Breve presentazione del relatore (minimo 200 caratteri) - (non mettete un link al curriculum ma scrivete per favore un testo completo)</span>
                <textarea id="form_input_propostarelatore_breve_ma_non_troppo_prese" name="form[breve_ma_non_troppo_prese]" class="form-textarea"></textarea>
                <span class="form-errormsg" style="display: none;">Questo è obbligatorio</span>
            </div>

            <div id="form_propostarelatore_telegram1" class="form-row form-text form-field-10">
                <label id="form_label_propostarelatore_telegram1" for="form_input_propostarelatore_telegram1" class="form-label">Telegram</label>
                <span class="form-helpmessage">Se si è in possesso di un profilo telegram inserire qui l'url identificativo del proprio profilo. (è opzionale, ma molto consigliato per semplificarci il lavoro di segreteria per contattarvi)</span>
                <input id="form_input_propostarelatore_telegram1" name="form[telegram1]" value="" class="form-input" type="text">
                <span class="form-errormsg" style="display: none;"></span>
            </div>

            <div id="form_propostarelatore_end" class="form-row form-freehtml form-field-11">
                <div id="form_input_propostarelatore_end" name="form[end]" value="" class="form-freehtml">
                    Ricordati di compilare uno di questi form per ogni autore che vuoi compaia nel programma

Ogni volta che compili questo form riceverai una mail di riepilogo, se non la ricevi entro una decina di minuti guarda nello SPAM, se non c'è scrivici riportando i dati presenti nel form.
                </div>
            </div>
        </div>

</details> <!-- SPEAKER -->
</div> <!-- SPEAKERS -->
	

	      <button type="button" id="addSpeaker">+ Aggiungi altro relatore</button>
	      <button type="button" id="removeSpeaker">− Rimuovi ultimo relatore</button>


            <div id="form_propostatalk_submit" class="form-row form-button-wrapper form-field-16">
                <button type="submit" name="form[submit]" id="form_input_propostatalk_submit" value="" class="form-button btn btn-default">Invio</button>
            </div>
	    
	    <font size="+1">
	    Se non ricevi la mail entro una decina di minuti con le istruzioni per la compilazione a) verifica nello spam b) prova a ricompilare il form o c) contatta gli organizzatori mandando un messaggio a segreteria@winstonsmith.org
	    </font>

            </div> <!== inner-form -->
        </div> <!-- form-page-wrapper -->

        <input type="hidden" name="form[formId]" id="form_propostatalk_id" value="22">
        <input type="hidden" name="form[return]" id="form_propostatalk_return" value="">
        <input type="hidden" name="form[formName]" id="form_propostatalk_name" value="propostatalk">

        </form>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
  // 1. Prendi l’input dell’email talk
  const talkEmail = document.getElementById('form_input_propostatalk_email_di_contatto_con_il');
  if (!talkEmail) return;

  // 2. Funzione per copiare nel primo relatore
  function syncFirstSpeakerEmail(val) {
    // seleziona dentro #speakers il primo .speaker il suo input email
    const firstEmail = document.querySelector('#speakers .speaker input[name="form[email]"]');
    if (firstEmail) firstEmail.value = val;
  }

  // 3. Al caricamento, copia se già valorizzato
  syncFirstSpeakerEmail(talkEmail.value);

  // 4. Aggancia l’evento input (scatta ad ogni digitazione)
  talkEmail.addEventListener('input', (e) => {
    syncFirstSpeakerEmail(e.target.value);
  });
});
</script>
