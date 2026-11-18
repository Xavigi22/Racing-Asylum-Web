from django.test import TestCase


class PaginaInicioTests(TestCase):
    def test_index2_con_barra_final_carga_su_plantilla(self):
        response = self.client.get('/index2/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ld_racingasylum/index2.html')
        self.assertContains(response, 'Bienvenido al sitio oficial de Racing Asylum')
        self.assertContains(response, 'Vehículos')
        self.assertContains(response, 'El juego')
        self.assertContains(response, 'Fecha de lanzamiento')
        self.assertContains(response, 'Copyright © 2026')

    def test_pagina_raiz_conserva_su_contenido(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Vehículos')
        self.assertContains(response, 'Copyright © 2026')
