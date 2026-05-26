const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

let gatos = [];
let nextId = 1;

// GET /cats → retorna todos los gatos
app.get('/cats', (req, res) => res.json(gatos));

// POST /cats → registra un gato nuevo
app.post('/cats', (req, res) => {
  const { nombre, edad, apodo } = req.body;
  const gato = { id: nextId++, nombre, edad, apodo };
  gatos.push(gato);
  res.status(201).json(gato);
});

// DELETE /cats/:id → elimina un gato
app.delete('/cats/:id', (req, res) => {
  const id = parseInt(req.params.id);
  gatos = gatos.filter(g => g.id !== id);
  res.json({ ok: true });
});

app.listen(3000, () => console.log('Backend de gatitos corriendo en puerto 3000 🐱'));