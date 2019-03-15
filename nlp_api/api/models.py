from flask_restplus import fields
from nlp_api.api import api

sample_text = '''European authorities fined Google a record $5.1 billion on Wednesday for abusing 
its power in the mobile phone market and ordered the company to alter its practices, in one 
of the most aggressive regulatory actions against American technology giants and one that 
may force lasting changes to smartphones. The European Union's antitrust fine of 4.34 billion 
euros was almost double the bloc's fine against Google last year over the company's unfair 
favoring of its own services in internet search results. The penalty's size highlighted 
Europe's increasingly bold stance against the power of American tech firms, even as officials 
in the United States have taken a largely hands-off approach to the companies. The fine was 
coupled with remedies that would effectively loosen Google's grip over its Android software, 
which is used in 80 percent of the world's smartphones and is a key part of the Silicon 
Valley company's business. Those changes, which European regulators ordered to take effect 
in 90 days, undercut Google's ability to automatically include its own search and other apps 
in mobile devices, opening it to more competition in a market that it has dominated. "Google 
has used Android as a vehicle to cement the dominance of its search engine," said 
Margrethe Vestager, Europe's antitrust chief. "These practices have denied rivals the chance 
to innovate and compete on the merits. They have denied European consumers the benefits of 
effective competition in the important mobile sphere." The size of the fine, she added, 
"reflects the seriousness and the sustained nature" of Google's actions. Google said it 
would appeal the decision, and the case is very likely to drag on for years. The company 
must deposit the fine in a holding account while the legal process unfolds. 
If Google ultimately loses an appeal, the money will be distributed among the European 
Union's member states. Regardless of an appeal, if Google does not start altering its mobile 
phone practices in 90 days, it faces penalties of up to 5 percent of the worldwide average 
daily revenue of its parent company, Alphabet. Sundar Pichai, Google's chief executive, 
said on Twitter that "rapid innovation, wide choice, and falling prices are classic hallmarks 
of robust competition." "Android has enabled this and created more choice for everyone, 
not less," he added. The long-anticipated ruling arrived at a politically delicate period, 
with Europe and the United States engaged in an escalating trade conflict in which both 
sides have imposed tariffs on an array of products, from alcohol to aluminum. 
Last week, on a trip to Brussels, President Trump reiterated his complaints that American 
businesses were at a disadvantage in Europe. Jean-Claude Juncker, president of the European 
Commission, the bloc's executive arm, is to visit Washington next week for 
talks with Mr. Trump. (Source: The New York Times)'''

text_model = api.model('text model', {
    'text': fields.String(description='Input text',
                          example='European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices.')
})

text_summaries_model = api.model('text summaries model', {
    'text': fields.String(description='Input text',
                          example=sample_text),
    'num_sentences': fields.Integer(description='Number of summary sentences',
                                    example=3)
})
