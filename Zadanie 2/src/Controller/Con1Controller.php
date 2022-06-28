<?php
namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class Con1Controller
{
    /**
     * @Route("/los", name="Con1")
     */
    public function number(): Response
    {
        $number = random_int(0, 10);

        return new Response(
            '<html>
			<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="opis" content="">
    <meta name="author" content="">

    <title>Słowo o Żabach</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet"
          href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css"
          integrity="sha384-Zug+QiDoJOrZ5t4lssLdxGhVrurbmBWopoEl+M6BdEfwnCJZtKxi1KgxUyJq13dy"
          crossorigin="anonymous">
</head>
<body>
			<header>
        <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
            <div class="container">

                <a class="navbar-brand" href="/">Strona główna</a>

                <div class="collapse navbar-collapse">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="/create">Dodaj Żabę</a>
                        </li>
						<li class="nav-item">
                            <a class="nav-link" href="/info">O Żabach</a>
                        </li>
						
						<li class="nav-item">
                            <a class="nav-link" href="/info">O Żabach</a>
                        </li>
						<li class="nav-item">
                            <a class="nav-link" href="/los">Losowanie</a>
                        </li>
                    </ul>
                </div>
            </div>

        </nav>
    </header>Numer dnia: '.$number.'</body></html>'
        );
    }
}