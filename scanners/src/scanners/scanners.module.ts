import { Module } from '@nestjs/common';
import { ScannersService } from './scanners.service';
import { ScannersController } from './scanners.controller';

@Module({
  providers: [ScannersService],
  controllers: [ScannersController]
})
export class ScannersModule {}
