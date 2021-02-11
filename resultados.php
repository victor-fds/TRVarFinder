<?php

	$str = file_get_contents('C:/Users/victo/Desktop/TCC/Finder/TRVarDetector/trf/resultados.json');	
	$json = json_decode($str, true); 
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
						<h4 class="col-md-2">Resultados</h4>
						<p class="col-md-9 mt-1">Tandem Repeats Variability Finder</p>
						<p>Estes são os TRs encontrados na sequência enviada, e seus respectivos índices de variabilidade.</p>
					</div>

					<div class="row mt-2">
						<hr>
						<h2 class="col-12 text-center">Resultado</h2>

						<table class="table">
							<thead>
								<tr>
									<th scope="col">#</th>
									<th scope="col">Var Encontrada</th>
									<th scope="col">Posição TR Começo->Final</th>
									<th scope="col">Tamanho do Repeat</th>
									<th scope="col">Pureza</th>
									<th scope="col">TRFScore</th>
								</tr>
							</thead>
							<tbody>
								<?php
									$i = 0;
									foreach ($json['prediction'] as $prediction) {
								?>
									<tr>
										<th scope="row"><?=$i;?></th>
										<td><?=$json['prediction'][$i];?></td>
										<td><?=$json['start'][$i];?>-><?=$json['end'][$i];?></td>
										<td><?=$json['consensus_size'][$i];?></td>
										<td><?=$json['purity'][$i];?>%</td>
										<td><?=$json['trf_score'][$i];?></td>
									</tr>
								<?php $i++; } ?>
							</tbody>
						</table>
					</div>
				</div>
			</div>
		</main>
		
		<footer style="background-color: #f2f2f2;" class="mt-5">
			<p class="text-dark text-center lead fs-6 p-3">TRVarFinder 2021 © Desenvolvido por Victor Fernandes; Vinicius Alves; Hugo Resende.</p>
		</footer>

		<!-- JavaScript Bundle with Popper -->
		<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>
	</body>

</html>