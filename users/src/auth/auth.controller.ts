import {
  Controller,
  Post,
  HttpCode, UseGuards,
  Request
} from '@nestjs/common';

import { LocalGuard } from './guards/local.guard';
import { AuthService } from './auth.service';
import { JwtGuard } from './guards/jwt.guard';

@Controller('auth')
export class AuthController {
  constructor(
    private readonly _authService: AuthService
  ) {}

  @UseGuards(LocalGuard)
  @Post('obtain_token')
  @HttpCode(200)
  async obtainToken(@Request() req) {
    return this._authService.login(req.user);
  }

  @UseGuards(JwtGuard)
  @Post('verify')
  @HttpCode(200)
  async verifyToken(@Request() req) {
    return req.user;
  }
}
