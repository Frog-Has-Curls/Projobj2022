namespace App\Controller;

use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class Con1Controller
{
    /**
     * @Route("/lucky/number/{max}", name="Con1")
     */
    public function number(int $max): Response
    {
        $number = random_int(0, $max);

        return new Response(
            '<html><body>NUmer dnia: '.$number.'</body></html>'
        );
    }
}