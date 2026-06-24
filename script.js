const checklistItems = document.querySelectorAll(".checklist label");
const storageKey = "ebike-field-guide:checked";

const savedState = new Set(JSON.parse(localStorage.getItem(storageKey) || "[]"));

checklistItems.forEach((label, index) => {
  const input = label.querySelector("input");
  input.checked = savedState.has(index);
  label.classList.toggle("is-checked", input.checked);

  input.addEventListener("change", () => {
    label.classList.toggle("is-checked", input.checked);

    const checked = [...checklistItems]
      .map((item, itemIndex) => (item.querySelector("input").checked ? itemIndex : null))
      .filter((itemIndex) => itemIndex !== null);

    localStorage.setItem(storageKey, JSON.stringify(checked));
  });
});
