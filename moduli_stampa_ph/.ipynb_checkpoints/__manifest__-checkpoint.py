# -*- coding: utf-8 -*-
{
    'name': "Moduli Stampa PH",

    'summary': """
        Modulo per aggiungere i report di Planet Horeca nel modulo Vendita.""",

    'description': """
        Modulo per aggiungere i report di Planet Horeca nel modulo Vendita, per stampare preventivi con e senza immagini dei prodotti. Inoltre, viene aggiunto un nuovo modello per la stampa dei DDT e viene collegato al bottone stampa, presente nel pannello DDT dell'ordine di vendita.""",

    'author': "Massimo Masi",
    'website': "https://www.abcstrategie.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'account',
                'sale',
                'stock',
                'partner_fax',
                'abc_codice_arca',
                'abc_codice_iva',
                'abc_x_planethoreca',
                'l10n_it_account',
                'l10n_it_delivery_note',
                'l10n_it_delivery_note_base',
                'l10n_it_delivery_note_batch',
                'l10n_it_delivery_note_order_link',
                'l10n_it_fatturapa',
                'l10n_it_fatturapa_in',
                'l10n_it_fatturapa_out',
                'l10n_it_fatturapa_sale',
                'l10n_it_fiscal_document_type',
                'l10n_it_fiscal_payment_term',
                'l10n_it_fiscalcode',
                'l10n_it_payment_reason',
                'l10n_it_pec',
                'l10n_it_rea'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/preventivo_paperformat.xml',
        'report/report_sale_order_ph.xml',
        'report/report_sale_order_wi_ph.xml',
        'report/ddt_ph.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
