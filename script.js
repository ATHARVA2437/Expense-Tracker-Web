const form = document.getElementById('expense-form');
const tableBody = document.getElementById('expense-table');

// Load expenses from localStorage
let expenses = JSON.parse(localStorage.getItem('expenses')) || [];
displayExpenses();

form.addEventListener('submit', function(e) {
  e.preventDefault();
  const category = document.getElementById('category').value;
  const amount = document.getElementById('amount').value;
  const description = document.getElementById('description').value;
  const date = new Date().toLocaleDateString();

  expenses.push({ date, category, amount, description });
  localStorage.setItem('expenses', JSON.stringify(expenses));
  displayExpenses();

  form.reset();
});

function displayExpenses() {
  tableBody.innerHTML = '';
  expenses.forEach(exp => {
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${exp.date}</td>
      <td>${exp.category}</td>
      <td>${exp.amount}</td>
      <td>${exp.description}</td>
    `;
    tableBody.appendChild(row);
  });
}
