// Работа с чекбоксами в таблицах

const select_all_checkboxes = document.getElementById('select-all');
const checkboxes = document.querySelectorAll('.table-checkbox');

// Выбрать/убрать чекбоксы
select_all_checkboxes.addEventListener('change', function() {
  checkboxes.forEach(checkbox => {
    checkbox.checked = this.checked;
  });
});

function delete_selected_rows() {
  const all_selected = document.querySelectorAll('.table-checkbox:checked');

  if(all_selected.length === 0) {
    alert('Нет выбранных данных для удаления');
    return;
  }

  if(confirm(`Вы уверены, что хотите удалить ${all_selected.length} запись(ей)?`)) {
    document.getElementById('deleteForm').submit();
  }
}