<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class Con2Controller extends AbstractController
{
    #[Route('/info', name: 'app_con2')]
    public function index(): Response
    {
        return $this->render('con2/index.html.twig', [
            'controller_name' => 'Con2Controller',
        ]);
    }
}
