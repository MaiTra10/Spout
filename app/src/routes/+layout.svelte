<script>
	import Header from './Header.svelte';
	import './styles.css';
	import '../app.css';
</script>

<div class="app">
	<Header />

	<main class="w-10/12 rounded-lg bg-white shadow-md shadow-slate-300">
		<slot />
	</main>

	<footer>
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
		align-items: center;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		margin: 0 auto;
		box-sizing: border-box;

	}


	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>
