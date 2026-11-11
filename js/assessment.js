/* Marketing assessment: scores 8 questions (Yes=2, Partly=1, No=0). */
(function () {
  'use strict';
  var form = document.getElementById('quiz');
  if (!form) return;
  var msg = document.getElementById('quizMsg');
  var box = document.getElementById('quizResult');
  var bands = [
    { max: 40, title: 'Your foundations need attention', text: 'There are big gaps that are likely costing you customers. The good news is that fixing the basics, such as your Google profile, tracking and follow-up, usually brings the quickest gains.' },
    { max: 65, title: 'You are getting there', text: 'Some things are working, but you are leaving enquiries on the table. A focused plan on tracking, local SEO and faster follow-up could lift results without a big budget.' },
    { max: 90, title: 'A strong base to build on', text: 'You have most of the essentials in place. The next step is optimisation: testing ads, improving conversion and putting more budget behind what already works.' },
    { max: 101, title: 'Excellent marketing health', text: 'You are doing most things right. A strategy call can uncover where scaling, new channels or AI search could add further growth.' }
  ];
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var total = 0, answered = 0, questions = form.querySelectorAll('.q');
    questions.forEach(function (q) {
      var c = q.querySelector('input:checked');
      q.style.borderColor = '';
      if (c) { total += parseInt(c.value, 10); answered++; } else { q.style.borderColor = '#ff5c6c'; }
    });
    if (answered < questions.length) {
      msg.textContent = 'Please answer all ' + questions.length + ' questions.';
      return;
    }
    msg.textContent = '';
    var pct = Math.round(total / (questions.length * 2) * 100);
    var band = bands.filter(function (b) { return pct < b.max; })[0] || bands[bands.length - 1];
    document.getElementById('qScore').textContent = pct + '/100';
    document.getElementById('qTitle').textContent = band.title;
    document.getElementById('qText').textContent = band.text;
    box.hidden = false;
    box.scrollIntoView({ behavior: 'smooth', block: 'center' });
  });
  form.addEventListener('change', function () { msg.textContent = ''; });
})();
