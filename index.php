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
						<p>Modelo desenvolvido para encontrar índices de variabilidade em Tandem Repeats genômicos, utilizando algoritmos de inteligência artificial para classificar as amostras. Este programa foi desenvolvido em Python, C e PHP.</p>
						<p></p>
					</div>

					<div class="row mt-2">
						<hr>
						<h2 class="col-12 text-center">Predição de Tandem Repeats e Variabilidade</h2>

						<form class="form" method="POST" action="pyexec">
							<div>
								<label for="fasta" class="mt-3">Digite aqui a sua sequencia que contém Tandem Repeats</label>
								<textarea id="fasta" name="fasta" class="mt-2 form-control" placeholder="Exemplo: 
>Descrição da sequencia em formato Fasta
AAAAAAGCTTGATCAAAAGAATTAGCTGAAATTAAAGCTGACGATGATAAAAAATTAGCAGAAGAAAATC" rows="5"></textarea>
							</div>
						
							<div class="col-4 mt-2">
								<label for="algoritmo" class="mb-1">Selecione um algoritmo de IA</label>
								<select id="algoritmo" name="algoritmo" class="form-select form-select-sm" aria-label=".form-select-sm example">
									<option value="knn">kNN (k-Nearest Neighbors)</option>
									<option value="svm">SVM (Support Vector Machine)</option>
								</select>
							</div>
							<div class="mt-4">
								<button class="btn w-25 btn-primary" type="submit">Enviar</button>
								<button class="btn btn-danger" type="reset">Limpar</button>
							</div>
						</form>
					</div>
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