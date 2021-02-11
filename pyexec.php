
<?php
	session_start();

	if(!empty($_POST['fasta']) && !empty($_POST['algoritmo'])){

		$string = strtoupper($_POST['fasta']);
		$string = explode("\n", $string);

		$check = ($string[0][0] == '>' && ($string[1][0] == 'A' || $string[1][0] == 'C' || $string[1][0] == 'T' || $string[1][0] == 'G'));
		
		if($check){
			$arquivo = fopen('/var/www/html/trvarfinder/py/trf/testar.fasta','w');

			if($arquivo != false){
				fwrite($arquivo, strtoupper($_POST['fasta']));
				fclose($arquivo);

				$caminho = dirname(__FILE__);
				$command = "python /var/www/html/trvarfinder/py/trf/main.py /var/www/html/trvarfinder/py/trf/testar.fasta";
				$output = passthru($command);

				header("location: resultados");
			} else
				$error = 1;
		} else 
			$error = 1;
	} else
		$error = 1;
?>

<html>

	<head>
		<!-- CSS only -->
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
	</head>

	<body>
		<header>
			<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
				<div class="container-fluid">
					<a class="navbar-brand" href="./home">TRVarFinder</a>
					<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>

					<div class="collapse navbar-collapse" id="navbarSupportedContent">
						<ul class="navbar-nav me-auto mb-2 mb-lg-0">
							<li class="nav-item">
								<a class="nav-link active" aria-current="page" href="./home">Página Inicial</a>
							</li>
							<li class="nav-item">
								<a class="nav-link" href="./sobre">Sobre</a>
							</li>
						</ul>
					</div>
				</div>
			</nav>
		</header>

		<main>
			<div class="d-flex justify-content-center">
				<div class="col-8">
					
					<div class="row mt-2">
						<h4 class="col-md-2">TRVarFinder</h4>
						<p class="col-md-9 mt-1">Tandem Repeats Variability Finder</p>
					</div>

					<?php if($error == 0){ ?>
					<div class="row mt-2  text-center justify-content-center">
						<hr>
						<h2 class="col-12">Executando</h2>
						<p>
							Aguarde um instante, sua entrada está sendo processada. 
							<div class="spinner-border text-warning  text-center" role="status">
							  <span class="visually-hidden">Loading...</span>
							</div>
						</p>
					</div>
					<?php } else { ?>
					<div class="row mt-2  text-center justify-content-center">
						<hr>
						<h2 class="col-12">Erro</h2>
						<p>
							Não foi possível executar o TRVarFinder com os parâmetros enviados. Verifique se a sua sequência está em formato .FASTA e tente novamente.
						</p>
						<a href="./home" class="btn btn-warning">Voltar</a>
					</div>
					<?php } ?>
				</div>
			</div>
		</main>
		
		<footer style="background-color: #f2f2f2;" class="mt-3">
			<p class="text-dark text-center lead fs-6 p-3">TRVarFinder 2021 © Desenvolvido por Victor Fernandes; Vinicius Alves; Hugo Resende.</p>
		</footer>

		<!-- JavaScript Bundle with Popper -->
		<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
	</body>

</html>