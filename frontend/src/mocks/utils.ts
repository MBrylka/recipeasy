export function delay(ms: number) {
    return new Promise( resolve => setTimeout(resolve, ms) );
}

export function getRandomNumber(min: number, max: number): number {
    return Math.random() * (max - min) + min;
  }

 export function getRandomBaseUnit(): string {
    const units = ["g", "ml", "pcs"];
    const randomIndex = Math.floor(Math.random() * units.length);
    return units[randomIndex];
  }