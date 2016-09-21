from config import unuseful_email_headings, useful_email_headings

class Email:

    def __init__(self, email_lines):
        self.email_lines = email_lines

        self.field_indices = {}
        for field in ['subject', 'from', 'to']:
            self.field_indices[field] = self.get_field_index(field)

        self.subject = self.get_field('subject')
        self.from_ = self.get_field('from')
        self.to_ = self.get_field('to')

        self.body = self.get_body()

    def __str__(self):
        try:
            return '\n\n'.join(["Subject: " + self.subject, 
                                "From: " + self.from_, 
                                "Body: " + self.body])
        except TypeError:
            return 'no email fields parsed, so nothing to print.'

    def get_field_index(self, field_name):
        line_starts_with = field_name.title() + ": "
        for index, line in enumerate(self.email_lines):
            if line.startswith(line_starts_with):
                return index

    def get_field(self, field_name):
        line_starts_with = field_name.title() + ": "
        field_index = self.field_indices[field_name]
        return self.email_lines[field_index].split(line_starts_with)[1]

    def get_body(self):
        #TODO: make this work
        all_headings = unuseful_email_headings + useful_email_headings
        for index, line in enumerate(self.email_lines):

            if (index > max(self.field_indices.values())
                    and not any(heading in line for heading in all_headings)):

                return '\n'.join([line
                                  for line in self.email_lines[index:]])

    def get_to(self):
        pass
