// Переход на страницу деталей одного файла по клику в таблице
document.addEventListener("DOMContentLoaded", function() {
  const rows = document.querySelectorAll("tr[data-href]");
    rows.forEach(row => {
      row.addEventListener("click", () => {
        window.location.href = row.dataset.href;
      });
    });
});

// Нормальный клик на чекбокс
document.querySelectorAll('tbody tr td:first-child input[type="checkbox"]').forEach(checkbox => {
  checkbox.addEventListener('click', function(event) {
    event.stopPropagation();
  });
});