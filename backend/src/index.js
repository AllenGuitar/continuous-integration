const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

let gatos = [];
let nextId = 1;

// trae los gatitos registrados
app.get('/cats', (req, res) => res.json(gatos));

// registro de nuevos gatitos
app.post('/cats', (req, res) => {
  const { nombre, edad, apodo } = req.body;
  const gato = { id: nextId++, nombre, edad, apodo };
  gatos.push(gato);
  res.status(201).json(gato);
});

app.delete('/cats/:id', (req, res) => {
  const id = parseInt(req.params.id);
  gatos = gatos.filter(g => g.id !== id);
  res.json({ ok: true });
});

app.listen(3000, () => console.log('Backend de gatitos corriendo en puerto 3000'));