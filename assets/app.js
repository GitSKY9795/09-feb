const output = document.getElementById('output');
const themeToggle = document.getElementById('toggleTheme');

const disclaimer =
  '\n\n⚠️ Medical disclaimer: This is educational guidance only. It does not diagnose disease or replace a licensed clinician.';

const templates = {
  fitness: `Fitness posture summary\n- Observed stance and alignment markers from uploaded image.\n- Possible imbalances: rounded shoulders / hip asymmetry / knee tracking.\n- Action plan: 3 corrective drills, 2 strength priorities, progressive load guidance.\n- Safety: stop if pain worsens and consult a qualified professional if persistent.`,
  medical: `Medical report simplification\n- Extracted key labs: CBC, glucose, lipids, thyroid, liver/kidney markers.\n- Plain-language explanation of high/low values with likely lifestyle factors.\n- Non-diagnostic risk flags and questions to discuss with your doctor.\n- Suggested next steps: hydration, sleep, nutrition tuning, follow-up tests cadence.`,
  prescription: `Prescription intelligence\n- Identified medicines and likely class/purpose.\n- Typical usage windows (morning/evening/with food) and spacing reminders.\n- Common side effects, interactions, and misuse warnings.\n- Advice: never self-adjust dosage; verify with prescribing doctor or pharmacist.`,
  plan: `Integrated weekly plan\n- Goal: blend fitness progress with reported medical considerations.\n- Training split: mobility + strength + low-impact cardio balance.\n- Diet direction: protein targets, fiber, sodium/sugar mindfulness, hydration timing.\n- Lifestyle anchors: sleep routine, stress reset protocol, habit tracker milestones.\n- Escalation triggers: when to pause exercise and seek professional care.`
};

function render(action) {
  const timestamp = new Date().toLocaleString();
  output.textContent = `${templates[action]}\n\nGenerated: ${timestamp}${disclaimer}`;
}

document.querySelectorAll('button[data-action]').forEach((button) => {
  button.addEventListener('click', () => render(button.dataset.action));
});

themeToggle.addEventListener('click', () => {
  document.documentElement.classList.toggle('dark');
});
