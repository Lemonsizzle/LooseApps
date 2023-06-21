import spacy
import tkinter as tk


class Redactor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text Redactor")

        self.entry = tk.Text(self, width=50, height=10, wrap="word")
        self.entry.pack(pady=20)

        self.redact_button = tk.Button(self, text="Redact", command=self.redact_text)
        self.redact_button.pack()

        options = tk.Frame(self)
        self.variables = {}
        entities = [
            "PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART",
            "LAW", "LANGUAGE", "DATE", "TIME", "PERCENT", "MONEY", "QUANTITY", "ORDINAL", "CARDINAL"]

        cols = 4

        for i, entity in enumerate(entities):
            # Create a BooleanVar for each entity
            self.variables[entity] = tk.BooleanVar()

            # Create a Checkbutton for each entity, positioned in a grid
            tk.Checkbutton(options, text=entity, variable=self.variables[entity]).grid(row=i // cols, column=i % cols)  # This will distribute the buttons in a grid layout

        self.variable_all = tk.BooleanVar()
        tk.Checkbutton(options, text="All", command=self.trigger_all, variable=self.variable_all)
        options.pack()

        self.result_label = tk.Label(self, text="Redacted Text will appear here.", wraplength=500)
        self.result_label.pack(pady=20)

    def trigger_all(self):
        value = self.variable_all.get()
        print(value)
        for entity, var in self.variables.items():
            var.set(value)

    def redact_text(self):
        text = self.entry.get("1.0", "end-1c")
        redacted_text, unredacted_items = self.redact_names(text)
        self.result_label['text'] = redacted_text
        with open('log.txt', 'w+') as f:
            f.write("Potential Classifications Errors:\n")
            for line in unredacted_items:
                f.write(line + "\n")

            f.write("In Text:\n")
            f.write(redacted_text)

    def redact_names(self, text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        redacted_sentence = text
        unredacted_items = []
        for ent in doc.ents:
            if self.variables[ent.label_].get():
                redacted_sentence = redacted_sentence.replace(ent.text, '[REDACTED]')
            else:
                unredacted_items.append(ent.text)
        print()
        return redacted_sentence, unredacted_items


if __name__ == "__main__":
    redactor_app = Redactor()
    redactor_app.mainloop()
