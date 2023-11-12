<script>
  export let card;
  let status = false;
  let auto =  false;

  function toggleAuto() {
    auto = !auto;
    console.log(auto);
  }

</script>

<div class="flex flex-col w-full max-w-7xl shadow-md shadow-gray-300 p-4 rounded-lg border-2 border-primary">
  <div class="grid grid-cols-3 justify-items-center items-center gap-4 border-b-2 border-black p-4">
    <div class="border-r-2 border-black w-full h-full flex flex-col justify-center items-start font-poppins">
      <h2>Spout Connected: {card.name}</h2>
      {#if auto}
        <button class="bg-green-500 w-20 rounded-md text-white" on:click={toggleAuto}>Auto</button>
      {:else}
        <button class="bg-red-500 w-20 rounded-md text-white" on:click={toggleAuto}>Auto</button>
      {/if}
    </div>
    <div class="border-r-2 border-black w-full h-full flex flex-col justify-center items-center font-poppins">
      <h2>Schedule</h2>
      <div class="flex">
        <div class="border-green-500 border-2 rounded-2xl p-2 text-center">
          <h2>Period</h2>
          <h2>Every {card.period} hrs</h2>
        </div>
      </div>
    </div>
    <div class="font-poppins">
      <div class="flex gap-4">
        <h2>Status: </h2>
        {#if status}
          <div class="bg-green-500 border-2 border-green-600 rounded-full text-center w-6 h-6 font-poppins">
            <h2>Active</h2>
          </div>
        {:else}
          <div class="bg-red-500 border-2 border-red-600 rounded-full text-center w-6 h-6 font-poppins"></div>
        {/if}
      </div>
      <div>
        <h2>Seed Type: </h2>
        <h2>{card.seed}</h2>
      </div>
    </div>    
  </div>
  <div class="grid grid-cols-2 place-items-center p-2 font-poppins">
    <div class="border-r-2 border-black w-full text-center">
      <h2>Recommended Watering Cycle</h2>
      <h2>(Base on Weather Information)</h2>
    </div>
    <div>
      <h2>Every {card.period} hours</h2>
      <h2>Watered Yesterday</h2>
    </div>
  </div>
</div>

